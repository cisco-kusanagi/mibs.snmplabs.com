#
# PySNMP MIB module ASCEND-MIBOSPFINR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBOSPFINR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:27:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, NotificationType, Integer32, Bits, ObjectIdentity, Counter64, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "NotificationType", "Integer32", "Bits", "ObjectIdentity", "Counter64", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibospfAreaRangeProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 97))
mibospfAreaRangeProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 97, 1), )
if mibBuilder.loadTexts: mibospfAreaRangeProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibospfAreaRangeProfileTable.setDescription('A list of mibospfAreaRangeProfile profile entries.')
mibospfAreaRangeProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1), ).setIndexNames((0, "ASCEND-MIBOSPFINR-MIB", "ospfAreaRangeProfile-Name"))
if mibBuilder.loadTexts: mibospfAreaRangeProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibospfAreaRangeProfileEntry.setDescription('A mibospfAreaRangeProfile entry containing objects that maps to the parameters of mibospfAreaRangeProfile profile.')
ospfAreaRangeProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 1), DisplayString()).setLabel("ospfAreaRangeProfile-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfAreaRangeProfile_Name.setStatus('mandatory')
if mibBuilder.loadTexts: ospfAreaRangeProfile_Name.setDescription('The name of this profile.')
ospfAreaRangeProfile_AreaId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 2), IpAddress()).setLabel("ospfAreaRangeProfile-AreaId").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfAreaRangeProfile_AreaId.setStatus('mandatory')
if mibBuilder.loadTexts: ospfAreaRangeProfile_AreaId.setDescription('Ospf area id for this area range.')
ospfAreaRangeProfile_AreaNetworkAddr = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 3), IpAddress()).setLabel("ospfAreaRangeProfile-AreaNetworkAddr").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfAreaRangeProfile_AreaNetworkAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ospfAreaRangeProfile_AreaNetworkAddr.setDescription('Ospf area network address.')
ospfAreaRangeProfile_AreaNetworkMask = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 4), IpAddress()).setLabel("ospfAreaRangeProfile-AreaNetworkMask").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfAreaRangeProfile_AreaNetworkMask.setStatus('mandatory')
if mibBuilder.loadTexts: ospfAreaRangeProfile_AreaNetworkMask.setDescription('Ospf area network mask.')
ospfAreaRangeProfile_Advertize = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ospfAreaRangeProfile-Advertize").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfAreaRangeProfile_Advertize.setStatus('mandatory')
if mibBuilder.loadTexts: ospfAreaRangeProfile_Advertize.setDescription('Indication of whether this area is to advertize.')
ospfAreaRangeProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ospfAreaRangeProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfAreaRangeProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: ospfAreaRangeProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBOSPFINR-MIB", ospfAreaRangeProfile_AreaId=ospfAreaRangeProfile_AreaId, mibospfAreaRangeProfileTable=mibospfAreaRangeProfileTable, ospfAreaRangeProfile_Advertize=ospfAreaRangeProfile_Advertize, ospfAreaRangeProfile_AreaNetworkMask=ospfAreaRangeProfile_AreaNetworkMask, ospfAreaRangeProfile_AreaNetworkAddr=ospfAreaRangeProfile_AreaNetworkAddr, ospfAreaRangeProfile_Name=ospfAreaRangeProfile_Name, mibospfAreaRangeProfileEntry=mibospfAreaRangeProfileEntry, ospfAreaRangeProfile_Action_o=ospfAreaRangeProfile_Action_o, mibospfAreaRangeProfile=mibospfAreaRangeProfile, DisplayString=DisplayString)
