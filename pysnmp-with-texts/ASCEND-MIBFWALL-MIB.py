#
# PySNMP MIB module ASCEND-MIBFWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBFWALL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:27:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, iso, TimeTicks, Integer32, Counter32, Unsigned32, ObjectIdentity, Counter64, NotificationType, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "iso", "TimeTicks", "Integer32", "Counter32", "Unsigned32", "ObjectIdentity", "Counter64", "NotificationType", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibfwallProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 79))
mibfwallProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 79, 1), )
if mibBuilder.loadTexts: mibfwallProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibfwallProfileTable.setDescription('A list of mibfwallProfile profile entries.')
mibfwallProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1), ).setIndexNames((0, "ASCEND-MIBFWALL-MIB", "fwallProfile-Name"))
if mibBuilder.loadTexts: mibfwallProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibfwallProfileEntry.setDescription('A mibfwallProfile entry containing objects that maps to the parameters of mibfwallProfile profile.')
fwallProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 1), DisplayString()).setLabel("fwallProfile-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: fwallProfile_Name.setStatus('mandatory')
if mibBuilder.loadTexts: fwallProfile_Name.setDescription('Descriptive name for this firewall.')
fwallProfile_Version = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 2), Integer32()).setLabel("fwallProfile-Version").setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallProfile_Version.setStatus('mandatory')
if mibBuilder.loadTexts: fwallProfile_Version.setDescription('The version number of software required to load this firewall.')
fwallProfile_Data = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 3), DisplayString()).setLabel("fwallProfile-Data").setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallProfile_Data.setStatus('mandatory')
if mibBuilder.loadTexts: fwallProfile_Data.setDescription('The actual contents of the FireWall.')
fwallProfile_Link = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 4), DisplayString()).setLabel("fwallProfile-Link").setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallProfile_Link.setStatus('mandatory')
if mibBuilder.loadTexts: fwallProfile_Link.setDescription('Link to an extension firewall profile.')
fwallProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("fwallProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: fwallProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBFWALL-MIB", fwallProfile_Action_o=fwallProfile_Action_o, fwallProfile_Name=fwallProfile_Name, fwallProfile_Version=fwallProfile_Version, fwallProfile_Link=fwallProfile_Link, mibfwallProfileEntry=mibfwallProfileEntry, DisplayString=DisplayString, fwallProfile_Data=fwallProfile_Data, mibfwallProfileTable=mibfwallProfileTable, mibfwallProfile=mibfwallProfile)
