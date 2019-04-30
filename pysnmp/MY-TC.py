#
# PySNMP MIB module MY-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
myModules, = mibBuilder.importSymbols("MY-SMI", "myModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, NotificationType, IpAddress, ModuleIdentity, Unsigned32, MibIdentifier, iso, Gauge32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "NotificationType", "IpAddress", "ModuleIdentity", "Unsigned32", "MibIdentifier", "iso", "Gauge32", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
myTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 4, 1))
myTextualConventions.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: myTextualConventions.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: myTextualConventions.setOrganization('D-Link Crop.')
class IfIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class MyTrapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("coldMy", 1), ("warmMy", 2), ("linkDown", 3), ("linkUp", 4), ("authenFailure", 5), ("newRoot", 6), ("topoChange", 7), ("hardChangeDetected", 8), ("portSecurityViolate", 9), ("stormAlarm", 10), ("macNotification", 11), ("vrrpNewMaster", 12), ("vrrpAuthFailure", 13), ("powerStateChange", 14), ("fanStateChange", 15), ("ospf", 16), ("pim", 17), ("igmp", 18), ("dvmrp", 19), ("entity", 20), ("cluster", 21), ("temperatureWarning", 22), ("sysGuard", 23), ("bgp", 24), ("lineDetect", 25), ("bgpReachMaxPrefix", 26), ("hardwareNotSupport", 27))

class ConfigStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("valid", 1), ("invalid", 2))

class MemberMap(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("MY-TC", IfIndex=IfIndex, MyTrapType=MyTrapType, PYSNMP_MODULE_ID=myTextualConventions, MemberMap=MemberMap, myTextualConventions=myTextualConventions, ConfigStatus=ConfigStatus)
