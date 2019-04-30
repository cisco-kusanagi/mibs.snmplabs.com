#
# PySNMP MIB module ASCEND-MIBOSPFINR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBOSPFINR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, ObjectIdentity, TimeTicks, Counter32, ModuleIdentity, Gauge32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "ObjectIdentity", "TimeTicks", "Counter32", "ModuleIdentity", "Gauge32", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibospfAreaRangeProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 97))
mibospfAreaRangeProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 97, 1), )
if mibBuilder.loadTexts: mibospfAreaRangeProfileTable.setStatus('mandatory')
mibospfAreaRangeProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1), ).setIndexNames((0, "ASCEND-MIBOSPFINR-MIB", "ospfAreaRangeProfile-Name"))
if mibBuilder.loadTexts: mibospfAreaRangeProfileEntry.setStatus('mandatory')
ospfAreaRangeProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 1), DisplayString()).setLabel("ospfAreaRangeProfile-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfAreaRangeProfile_Name.setStatus('mandatory')
ospfAreaRangeProfile_AreaId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 2), IpAddress()).setLabel("ospfAreaRangeProfile-AreaId").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfAreaRangeProfile_AreaId.setStatus('mandatory')
ospfAreaRangeProfile_AreaNetworkAddr = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 3), IpAddress()).setLabel("ospfAreaRangeProfile-AreaNetworkAddr").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfAreaRangeProfile_AreaNetworkAddr.setStatus('mandatory')
ospfAreaRangeProfile_AreaNetworkMask = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 4), IpAddress()).setLabel("ospfAreaRangeProfile-AreaNetworkMask").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfAreaRangeProfile_AreaNetworkMask.setStatus('mandatory')
ospfAreaRangeProfile_Advertize = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ospfAreaRangeProfile-Advertize").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfAreaRangeProfile_Advertize.setStatus('mandatory')
ospfAreaRangeProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 97, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ospfAreaRangeProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfAreaRangeProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBOSPFINR-MIB", ospfAreaRangeProfile_Action_o=ospfAreaRangeProfile_Action_o, ospfAreaRangeProfile_Advertize=ospfAreaRangeProfile_Advertize, ospfAreaRangeProfile_AreaNetworkAddr=ospfAreaRangeProfile_AreaNetworkAddr, ospfAreaRangeProfile_AreaNetworkMask=ospfAreaRangeProfile_AreaNetworkMask, DisplayString=DisplayString, mibospfAreaRangeProfileEntry=mibospfAreaRangeProfileEntry, mibospfAreaRangeProfile=mibospfAreaRangeProfile, ospfAreaRangeProfile_Name=ospfAreaRangeProfile_Name, ospfAreaRangeProfile_AreaId=ospfAreaRangeProfile_AreaId, mibospfAreaRangeProfileTable=mibospfAreaRangeProfileTable)
