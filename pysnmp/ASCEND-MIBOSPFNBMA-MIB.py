#
# PySNMP MIB module ASCEND-MIBOSPFNBMA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBOSPFNBMA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, iso, ObjectIdentity, Gauge32, Unsigned32, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, TimeTicks, NotificationType, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "ObjectIdentity", "Gauge32", "Unsigned32", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "TimeTicks", "NotificationType", "ModuleIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibospfNbmaNeighborProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 98))
mibospfNbmaNeighborProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 98, 1), )
if mibBuilder.loadTexts: mibospfNbmaNeighborProfileTable.setStatus('mandatory')
mibospfNbmaNeighborProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1), ).setIndexNames((0, "ASCEND-MIBOSPFNBMA-MIB", "ospfNbmaNeighborProfile-Name"))
if mibBuilder.loadTexts: mibospfNbmaNeighborProfileEntry.setStatus('mandatory')
ospfNbmaNeighborProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 1), DisplayString()).setLabel("ospfNbmaNeighborProfile-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_Name.setStatus('mandatory')
ospfNbmaNeighborProfile_HostName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 2), DisplayString()).setLabel("ospfNbmaNeighborProfile-HostName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_HostName.setStatus('mandatory')
ospfNbmaNeighborProfile_IpAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 3), IpAddress()).setLabel("ospfNbmaNeighborProfile-IpAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_IpAddress.setStatus('mandatory')
ospfNbmaNeighborProfile_DrCapable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ospfNbmaNeighborProfile-DrCapable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_DrCapable.setStatus('mandatory')
ospfNbmaNeighborProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ospfNbmaNeighborProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBOSPFNBMA-MIB", ospfNbmaNeighborProfile_HostName=ospfNbmaNeighborProfile_HostName, ospfNbmaNeighborProfile_IpAddress=ospfNbmaNeighborProfile_IpAddress, mibospfNbmaNeighborProfileEntry=mibospfNbmaNeighborProfileEntry, ospfNbmaNeighborProfile_DrCapable=ospfNbmaNeighborProfile_DrCapable, mibospfNbmaNeighborProfile=mibospfNbmaNeighborProfile, DisplayString=DisplayString, ospfNbmaNeighborProfile_Action_o=ospfNbmaNeighborProfile_Action_o, ospfNbmaNeighborProfile_Name=ospfNbmaNeighborProfile_Name, mibospfNbmaNeighborProfileTable=mibospfNbmaNeighborProfileTable)
