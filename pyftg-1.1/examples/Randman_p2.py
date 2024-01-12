import numpy as np
from pyftg import *
from PowerManager import PowerManager
import datetime




class Randman_p2(AIInterface):
    def __init__(self):
        super().__init__()
        self.blind_flag = True
        self.round_count = 0

        #LV1 : panch kick jump skill X
        self.actions_lv1 = (
            # "AIR_A",          #kutyuu deno karui panch
            # "AIR_B",          #kutyuu deno karui kick
            # "AIR_D_DB_BA",    #kutyuu zensin tuyo panch
            # "AIR_D_DB_BB",    #kutyuu zensin tuyo kick
            # "AIR_D_DF_FA",    #kutyuu yowa fire ball
            # "AIR_D_DF_FB",    #kutyuu tuyo fire ball
            # "AIR_DA",         #kutyuu deno karui sita panch
            # "AIR_DB",         #kutyuu deno karui sita kick
            # "AIR_F_D_DFA",    #kutyuu zensin yowa panch
            # "AIR_F_D_DFB",    #kutyuu zensin yowa kick
            # "AIR_FA",         #kutyuu deno tyu panch
            # "AIR_FB",         #kutyuu deno tyu kick 
            # "AIR_UA",         #kutyuu deno tuyo panch
            # "AIR_UB",         #kutyuu deno tuyo kick
            # "BACK_JUMP",      

            "BACK_STEP",
            # "CROUCH_A",       #shagami yowa panch
            # "CROUCH_B",       #shagami yowa kick
            # "CROUCH_FA",      #shagami karano upper
            # "CROUCH_FB",      #shagami tuyo kick
            "CROUCH_GUARD",   #sitakougeki guard
            "DASH",
            # "FOR_JUMP",       #mae jump
            "FORWARD_WALK",   #mae aruki
            # "JUMP",
            "NEUTRAL",        #nanimosinai
            # "STAND_A",        #karui panch
            # "STAND_B",        #karui kick 
            # "STAND_D_DB_BA",  #jump kougeki
            # "STAND_D_DB_BB",  #slide kick
            # "STAND_D_DF_FA",  #yowa fire ball
            # "STAND_D_DF_FB",  #tuyo fire ball  
            # "STAND_D_DF_FC",  #special fire ball
            # "STAND_F_D_DFA",  #upper karano shagami
            # "STAND_F_D_DFB",  #tuyo upper
            # "STAND_FA",       #tuyo panch  
            # "STAND_FB",       #tuyo kick
            "STAND_GUARD",    #mannakakougeki guard
            "THROW_A",        #karui nage
            "THROW_B",        #hagesi nage
        )


        #LV2 : kick jump skill X
        self.actions_lv2 = (
            # "AIR_A",          #kutyuu deno karui panch
            # "AIR_B",          #kutyuu deno karui kick
            # "AIR_D_DB_BA",    #kutyuu zensin tuyo panch
            # "AIR_D_DB_BB",    #kutyuu zensin tuyo kick
            # "AIR_D_DF_FA",    #kutyuu yowa fire ball
            # "AIR_D_DF_FB",    #kutyuu tuyo fire ball
            # "AIR_DA",         #kutyuu deno karui sita panch
            # "AIR_DB",         #kutyuu deno karui sita kick
            # "AIR_F_D_DFA",    #kutyuu zensin yowa panch
            # "AIR_F_D_DFB",    #kutyuu zensin yowa kick
            # "AIR_FA",         #kutyuu deno tyu panch
            # "AIR_FB",         #kutyuu deno tyu kick 
            # "AIR_UA",         #kutyuu deno tuyo panch
            # "AIR_UB",         #kutyuu deno tuyo kick
            # "BACK_JUMP",      

            "BACK_STEP",
            "CROUCH_A",       #shagami yowa panch
            # "CROUCH_B",       #shagami yowa kick
            "CROUCH_FA",      #shagami karano upper
            # "CROUCH_FB",      #shagami tuyo kick
            "CROUCH_GUARD",   #sitakougeki guard
            "DASH",
            # "FOR_JUMP",       #mae jump
            "FORWARD_WALK",   #mae aruki
            # "JUMP",
            "NEUTRAL",        #nanimosinai
            "STAND_A",        #karui panch
            # "STAND_B",        #karui kick 
            # "STAND_D_DB_BA",  #jump kougeki
            # "STAND_D_DB_BB",  #slide kick
            # "STAND_D_DF_FA",  #yowa fire ball
            # "STAND_D_DF_FB",  #tuyo fire ball  
            # "STAND_D_DF_FC",  #special fire ball
            "STAND_F_D_DFA",  #upper karano shagami
            "STAND_F_D_DFB",  #tuyo upper
            "STAND_FA",       #tuyo panch  
            # "STAND_FB",       #tuyo kick
            "STAND_GUARD",    #mannakakougeki guard
            "THROW_A",        #karui nage
            "THROW_B",        #hagesi nage
        )


        #LV3 : jump skill X
        self.actions_lv3 = (
            # "AIR_A",          #kutyuu deno karui panch
            # "AIR_B",          #kutyuu deno karui kick
            # "AIR_D_DB_BA",    #kutyuu zensin tuyo panch
            # "AIR_D_DB_BB",    #kutyuu zensin tuyo kick
            # "AIR_D_DF_FA",    #kutyuu yowa fire ball
            # "AIR_D_DF_FB",    #kutyuu tuyo fire ball
            # "AIR_DA",         #kutyuu deno karui sita panch
            # "AIR_DB",         #kutyuu deno karui sita kick
            # "AIR_F_D_DFA",    #kutyuu zensin yowa panch
            # "AIR_F_D_DFB",    #kutyuu zensin yowa kick
            # "AIR_FA",         #kutyuu deno tyu panch
            # "AIR_FB",         #kutyuu deno tyu kick 
            # "AIR_UA",         #kutyuu deno tuyo panch
            # "AIR_UB",         #kutyuu deno tuyo kick
            # "BACK_JUMP",      

            "BACK_STEP",
            "CROUCH_A",       #shagami yowa panch
            "CROUCH_B",       #shagami yowa kick
            "CROUCH_FA",      #shagami karano upper
            "CROUCH_FB",      #shagami tuyo kick
            "CROUCH_GUARD",   #sitakougeki guard
            "DASH",
            # "FOR_JUMP",       #mae jump
            "FORWARD_WALK",   #mae aruki
            # "JUMP",
            "NEUTRAL",        #nanimosinai
            "STAND_A",        #karui panch
            "STAND_B",        #karui kick 
            # "STAND_D_DB_BA",  #jump kougeki
            "STAND_D_DB_BB",  #slide kick
            # "STAND_D_DF_FA",  #yowa fire ball
            # "STAND_D_DF_FB",  #tuyo fire ball  
            # "STAND_D_DF_FC",  #special fire ball
            "STAND_F_D_DFA",  #upper karano shagami
            "STAND_F_D_DFB",  #tuyo upper
            "STAND_FA",       #tuyo panch  
            "STAND_FB",       #tuyo kick
            "STAND_GUARD",    #mannakakougeki guard
            "THROW_A",        #karui nage
            "THROW_B",        #hagesi nage
        )


        #LV4 : skill X
        self.actions_lv4 = (
            "AIR_A",          #kutyuu deno karui panch
            "AIR_B",          #kutyuu deno karui kick
            "AIR_D_DB_BA",    #kutyuu zensin tuyo panch
            "AIR_D_DB_BB",    #kutyuu zensin tuyo panch
            "AIR_D_DF_FA",    #kutyuu yowa fire ball
            "AIR_D_DF_FB",    #kutyuu tuyo fire ball
            "AIR_DA",         #kutyuu deno karui sita panch
            "AIR_DB",         #kutyuu deno karui sita kick
            "AIR_F_D_DFA",    #kutyuu zensin yowa panch
            "AIR_F_D_DFB",    #kutyuu zensin yowa kick
            "AIR_FA",         #kutyuu deno tyu panch
            "AIR_FB",         #kutyuu deno tyu kick 
            "AIR_UA",         #kutyuu deno tuyo panch
            "AIR_UB",         #kutyuu deno tuyo kick
            "BACK_JUMP",      
            "BACK_STEP",
            "CROUCH_A",       #shagami yowa panch
            "CROUCH_B",       #shagami yowa kick
            "CROUCH_FA",      #shagami karano upper
            "CROUCH_FB",      #shagami tuyo kick
            "CROUCH_GUARD",   #sitakougeki guard
            "DASH",
            "FOR_JUMP",       #mae jump
            "FORWARD_WALK",   #mae aruki
            "JUMP",
            "NEUTRAL",        #nanimosinai
            "STAND_A",        #karui panch
            "STAND_B",        #karui kick 
            "STAND_D_DB_BA",  #jump kougeki
            "STAND_D_DB_BB",  #slide kick
            # "STAND_D_DF_FA",  #yowa fire ball
            # "STAND_D_DF_FB",  #tuyo fire ball  
            # "STAND_D_DF_FC",  #special fire ball
            "STAND_F_D_DFA",  #upper karano shagami
            "STAND_F_D_DFB",  #tuyo upper
            "STAND_FA",       #tuyo panch  
            "STAND_FB",       #tuyo kick
            "STAND_GUARD",    #mannakakougeki guard
            "THROW_A",        #karui nage
            "THROW_B",        #hagesi nage
        )


        #LV5 : 
        self.actions_lv5 = (
            "AIR_A",          #kutyuu deno karui panch
            "AIR_B",          #kutyuu deno karui kick
            "AIR_D_DB_BA",    #kutyuu zensin tuyo panch
            "AIR_D_DB_BB",    #kutyuu zensin tuyo panch
            "AIR_D_DF_FA",    #kutyuu yowa fire ball
            "AIR_D_DF_FB",    #kutyuu tuyo fire ball
            "AIR_DA",         #kutyuu deno karui sita panch
            "AIR_DB",         #kutyuu deno karui sita kick
            "AIR_F_D_DFA",    #kutyuu zensin yowa panch
            "AIR_F_D_DFB",    #kutyuu zensin yowa kick
            "AIR_FA",         #kutyuu deno tyu panch
            "AIR_FB",         #kutyuu deno tyu kick 
            "AIR_UA",         #kutyuu deno tuyo panch
            "AIR_UB",         #kutyuu deno tuyo kick
            "BACK_JUMP",      
            "BACK_STEP",
            "CROUCH_A",       #shagami yowa panch
            "CROUCH_B",       #shagami yowa kick
            "CROUCH_FA",      #shagami karano upper
            "CROUCH_FB",      #shagami tuyo kick
            "CROUCH_GUARD",   #sitakougeki guard
            "DASH",
            "FOR_JUMP",       #mae jump
            "FORWARD_WALK",   #mae aruki
            "JUMP",
            "NEUTRAL",        #nanimosinai
            "STAND_A",        #karui panch
            "STAND_B",        #karui kick 
            "STAND_D_DB_BA",  #jump kougeki
            "STAND_D_DB_BB",  #slide kick
            "STAND_D_DF_FA",  #yowa fire ball
            "STAND_D_DF_FB",  #tuyo fire ball  
            "STAND_D_DF_FC",  #special fire ball
            "STAND_F_D_DFA",  #upper karano shagami
            "STAND_F_D_DFB",  #tuyo upper
            "STAND_FA",       #tuyo panch  
            "STAND_FB",       #tuyo kick
            "STAND_GUARD",    #mannakakougeki guard
            "THROW_A",        #karui nage
            "THROW_B",        #hagesi nage
        )


        self.last_time = datetime.datetime.utcnow()
        self.level = 3
        self.wait_time = 10   #s

        self.i = 0
        self.date = ["2023-12-1 15:35:40", "2023-12-1 15:35:46", "2023-12-1 15:35:53", "2023-12-1 15:36:00", "2023-12-1 15:36:5"]

        self.powermanager = PowerManager(0, "p2")

    def name(self) -> str:
        return self.__class__.__name__

    def is_blind(self) -> bool:
        return self.blind_flag

    def initialize(self, game_data: GameData, player_number: int):
        self.cc = CommandCenter()
        self.inputKey = Key()
        self.player = player_number
        self.isGameJustStarted = True
        return 0

    def input(self) -> Key:
        return self.inputKey

    def get_information(
        self, frame_data: FrameData, is_control: bool, non_delay_frame_data: FrameData
    ):
        self.frame_data = frame_data
        self.cc.set_frame_data(self.frame_data, self.player)

    def get_screen_data(self, screen_data: ScreenData):
        self.screen_data = screen_data

    def get_audio_data(self, audio_data: AudioData):
        self.audio_data = audio_data


    def processing(self):

        if  (self.last_time + datetime.timedelta(seconds=self.wait_time)) <= datetime.datetime.utcnow():
            self.level = self.powermanager.askLevel(self.wait_time, "now")
            self.last_time = datetime.datetime.utcnow()

        #if (self.last_time + datetime.timedelta(seconds=10)) <= datetime.datetime.utcnow():
        #    self.level = self.powermanager.askLevel(self.wait_time, self.date[self.i])
        #    #print(self.i, self.level)
        #    self.i += 1
        #    self.last_time = datetime.datetime.utcnow()


        self.inputKey.empty()
        self.cc.skill_cancel()

        if self.level == 1:
            self.cc.command_call(np.random.choice(self.actions_lv1))
        elif self.level == 2:
            self.cc.command_call(np.random.choice(self.actions_lv2))
        elif self.level == 3:
            self.cc.command_call(np.random.choice(self.actions_lv3))
        elif self.level == 4:
            self.cc.command_call(np.random.choice(self.actions_lv4))
        else:
            self.cc.command_call(np.random.choice(self.actions_lv5))


        self.inputKey = self.cc.get_skill_key()
        

    def round_end(self, round_result: RoundResult):
        print(round_result.remaining_hps[0])
        print(round_result.remaining_hps[1])
        print(round_result.elapsed_frame)
        self.round_count += 1
        print(f"Finished {self.round_count} round for {self.name()}")

    def game_end(self):
        self.powermanager.disconnect()
        pass
