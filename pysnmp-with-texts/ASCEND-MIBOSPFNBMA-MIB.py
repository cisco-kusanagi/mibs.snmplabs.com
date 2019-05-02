#
# PySNMP MIB module ASCEND-MIBOSPFNBMA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBOSPFNBMA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:27:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Integer32, TimeTicks, Unsigned32, NotificationType, Counter32, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Counter64, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "TimeTicks", "Unsigned32", "NotificationType", "Counter32", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Counter64", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibospfNbmaNeighborProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 98))
mibospfNbmaNeighborProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 98, 1), )
if mibBuilder.loadTexts: mibospfNbmaNeighborProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibospfNbmaNeighborProfileTable.setDescription('A list of mibospfNbmaNeighborProfile profile entries.')
mibospfNbmaNeighborProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1), ).setIndexNames((0, "ASCEND-MIBOSPFNBMA-MIB", "ospfNbmaNeighborProfile-Name"))
if mibBuilder.loadTexts: mibospfNbmaNeighborProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibospfNbmaNeighborProfileEntry.setDescription('A mibospfNbmaNeighborProfile entry containing objects that maps to the parameters of mibospfNbmaNeighborProfile profile.')
ospfNbmaNeighborProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 1), DisplayString()).setLabel("ospfNbmaNeighborProfile-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_Name.setStatus('mandatory')
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_Name.setDescription('The name of this profile.')
ospfNbmaNeighborProfile_HostName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 2), DisplayString()).setLabel("ospfNbmaNeighborProfile-HostName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_HostName.setStatus('mandatory')
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_HostName.setDescription('The name of the associated connection profile.')
ospfNbmaNeighborProfile_IpAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 3), IpAddress()).setLabel("ospfNbmaNeighborProfile-IpAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_IpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_IpAddress.setDescription("The neighbor's IP address.")
ospfNbmaNeighborProfile_DrCapable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ospfNbmaNeighborProfile-DrCapable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_DrCapable.setStatus('mandatory')
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_DrCapable.setDescription('Can the neighbor be a Designated Router?')
ospfNbmaNeighborProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 98, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ospfNbmaNeighborProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: ospfNbmaNeighborProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBOSPFNBMA-MIB", ospfNbmaNeighborProfile_Name=ospfNbmaNeighborProfile_Name, ospfNbmaNeighborProfile_DrCapable=ospfNbmaNeighborProfile_DrCapable, mibospfNbmaNeighborProfileTable=mibospfNbmaNeighborProfileTable, ospfNbmaNeighborProfile_Action_o=ospfNbmaNeighborProfile_Action_o, DisplayString=DisplayString, ospfNbmaNeighborProfile_IpAddress=ospfNbmaNeighborProfile_IpAddress, mibospfNbmaNeighborProfile=mibospfNbmaNeighborProfile, ospfNbmaNeighborProfile_HostName=ospfNbmaNeighborProfile_HostName, mibospfNbmaNeighborProfileEntry=mibospfNbmaNeighborProfileEntry)
