import com.erudika.para.cache.HazelcastCache;
import com.hazelcast.config.Config;
import com.hazelcast.core.Hazelcast;
import com.hazelcast.config.XmlConfigBuilder;
public class ReachabilityTest {
    public static void main(String args[]){
        Test ins = new Test();
        XmlConfigBuilder ins2 = new XmlConfigBuilder();
        Config d = ins2.build();
        d.getCacheConfigs();
        ins.rs();
    }
    public static class Test extends  HazelcastCache{
        Test(){
            super();
        }
        public void rs(){
            XmlConfigBuilder ins2 = new XmlConfigBuilder();
        }
    }
}
