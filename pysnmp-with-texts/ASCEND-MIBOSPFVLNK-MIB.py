#
# PySNMP MIB module ASCEND-MIBOSPFVLNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBOSPFVLNK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:27:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, Unsigned32, IpAddress, Integer32, NotificationType, ObjectIdentity, MibIdentifier, Bits, ModuleIdentity, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Unsigned32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "MibIdentifier", "Bits", "ModuleIdentity", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibospfVirtIntfProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 99))
mibospfVirtIntfProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 99, 1), )
if mibBuilder.loadTexts: mibospfVirtIntfProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibospfVirtIntfProfileTable.setDescription('A list of mibospfVirtIntfProfile profile entries.')
mibospfVirtIntfProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1), ).setIndexNames((0, "ASCEND-MIBOSPFVLNK-MIB", "ospfVirtIntfProfile-NeighborRouterId"))
if mibBuilder.loadTexts: mibospfVirtIntfProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibospfVirtIntfProfileEntry.setDescription('A mibospfVirtIntfProfile entry containing objects that maps to the parameters of mibospfVirtIntfProfile profile.')
ospfVirtIntfProfile_NeighborRouterId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 1), IpAddress()).setLabel("ospfVirtIntfProfile-NeighborRouterId").setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfVirtIntfProfile_NeighborRouterId.setStatus('mandatory')
if mibBuilder.loadTexts: ospfVirtIntfProfile_NeighborRouterId.setDescription('Ospf virtual link neighbor router id.')
ospfVirtIntfProfile_TransitAreaId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 2), IpAddress()).setLabel("ospfVirtIntfProfile-TransitAreaId").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfVirtIntfProfile_TransitAreaId.setStatus('mandatory')
if mibBuilder.loadTexts: ospfVirtIntfProfile_TransitAreaId.setDescription('Ospf virtual link transit area id.')
ospfVirtIntfProfile_RexmitDelay = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 3), Integer32()).setLabel("ospfVirtIntfProfile-RexmitDelay").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfVirtIntfProfile_RexmitDelay.setStatus('mandatory')
if mibBuilder.loadTexts: ospfVirtIntfProfile_RexmitDelay.setDescription('Ospf virtual link re-xmit delay.')
ospfVirtIntfProfile_XmitDelay = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 4), Integer32()).setLabel("ospfVirtIntfProfile-XmitDelay").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfVirtIntfProfile_XmitDelay.setStatus('mandatory')
if mibBuilder.loadTexts: ospfVirtIntfProfile_XmitDelay.setDescription('Ospf virtual link xmit delay.')
ospfVirtIntfProfile_HelloInterval = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 5), Integer32()).setLabel("ospfVirtIntfProfile-HelloInterval").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfVirtIntfProfile_HelloInterval.setStatus('mandatory')
if mibBuilder.loadTexts: ospfVirtIntfProfile_HelloInterval.setDescription('Ospf virtual link hello packet interval.')
ospfVirtIntfProfile_DeadInterval = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 6), Integer32()).setLabel("ospfVirtIntfProfile-DeadInterval").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfVirtIntfProfile_DeadInterval.setStatus('mandatory')
if mibBuilder.loadTexts: ospfVirtIntfProfile_DeadInterval.setDescription('Ospf virtual link dead interval.')
ospfVirtIntfProfile_AuthenType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("simple", 2), ("md5", 3)))).setLabel("ospfVirtIntfProfile-AuthenType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfVirtIntfProfile_AuthenType.setStatus('mandatory')
if mibBuilder.loadTexts: ospfVirtIntfProfile_AuthenType.setDescription('Ospf virtual link authentication type.')
ospfVirtIntfProfile_AuthenKey = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 8), DisplayString()).setLabel("ospfVirtIntfProfile-AuthenKey").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfVirtIntfProfile_AuthenKey.setStatus('mandatory')
if mibBuilder.loadTexts: ospfVirtIntfProfile_AuthenKey.setDescription('Ospf virtual link authentication key.')
ospfVirtIntfProfile_KeyId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 9), Integer32()).setLabel("ospfVirtIntfProfile-KeyId").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfVirtIntfProfile_KeyId.setStatus('mandatory')
if mibBuilder.loadTexts: ospfVirtIntfProfile_KeyId.setDescription('Ospf virtual link MD5 authentication key.')
ospfVirtIntfProfile_Md5AuthenKey = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 10), DisplayString()).setLabel("ospfVirtIntfProfile-Md5AuthenKey").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfVirtIntfProfile_Md5AuthenKey.setStatus('mandatory')
if mibBuilder.loadTexts: ospfVirtIntfProfile_Md5AuthenKey.setDescription('Ospf virtual link MD5 authentication key.')
ospfVirtIntfProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ospfVirtIntfProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfVirtIntfProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: ospfVirtIntfProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBOSPFVLNK-MIB", mibospfVirtIntfProfile=mibospfVirtIntfProfile, ospfVirtIntfProfile_HelloInterval=ospfVirtIntfProfile_HelloInterval, ospfVirtIntfProfile_AuthenKey=ospfVirtIntfProfile_AuthenKey, ospfVirtIntfProfile_Md5AuthenKey=ospfVirtIntfProfile_Md5AuthenKey, ospfVirtIntfProfile_DeadInterval=ospfVirtIntfProfile_DeadInterval, ospfVirtIntfProfile_Action_o=ospfVirtIntfProfile_Action_o, DisplayString=DisplayString, mibospfVirtIntfProfileEntry=mibospfVirtIntfProfileEntry, ospfVirtIntfProfile_KeyId=ospfVirtIntfProfile_KeyId, ospfVirtIntfProfile_NeighborRouterId=ospfVirtIntfProfile_NeighborRouterId, ospfVirtIntfProfile_AuthenType=ospfVirtIntfProfile_AuthenType, mibospfVirtIntfProfileTable=mibospfVirtIntfProfileTable, ospfVirtIntfProfile_TransitAreaId=ospfVirtIntfProfile_TransitAreaId, ospfVirtIntfProfile_RexmitDelay=ospfVirtIntfProfile_RexmitDelay, ospfVirtIntfProfile_XmitDelay=ospfVirtIntfProfile_XmitDelay)
