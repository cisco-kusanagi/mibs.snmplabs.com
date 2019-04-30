#
# PySNMP MIB module ASCEND-MIBFWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBFWALL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Bits, Unsigned32, IpAddress, Integer32, iso, Gauge32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Unsigned32", "IpAddress", "Integer32", "iso", "Gauge32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibfwallProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 79))
mibfwallProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 79, 1), )
if mibBuilder.loadTexts: mibfwallProfileTable.setStatus('mandatory')
mibfwallProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1), ).setIndexNames((0, "ASCEND-MIBFWALL-MIB", "fwallProfile-Name"))
if mibBuilder.loadTexts: mibfwallProfileEntry.setStatus('mandatory')
fwallProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 1), DisplayString()).setLabel("fwallProfile-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: fwallProfile_Name.setStatus('mandatory')
fwallProfile_Version = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 2), Integer32()).setLabel("fwallProfile-Version").setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallProfile_Version.setStatus('mandatory')
fwallProfile_Data = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 3), DisplayString()).setLabel("fwallProfile-Data").setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallProfile_Data.setStatus('mandatory')
fwallProfile_Link = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 4), DisplayString()).setLabel("fwallProfile-Link").setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallProfile_Link.setStatus('mandatory')
fwallProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("fwallProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: fwallProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBFWALL-MIB", fwallProfile_Version=fwallProfile_Version, fwallProfile_Link=fwallProfile_Link, fwallProfile_Data=fwallProfile_Data, mibfwallProfileTable=mibfwallProfileTable, fwallProfile_Name=fwallProfile_Name, fwallProfile_Action_o=fwallProfile_Action_o, mibfwallProfileEntry=mibfwallProfileEntry, DisplayString=DisplayString, mibfwallProfile=mibfwallProfile)
