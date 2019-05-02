#
# PySNMP MIB module ASCEND-MIBB52TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBB52TEST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, MibIdentifier, Bits, Counter32, iso, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, IpAddress, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "MibIdentifier", "Bits", "Counter32", "iso", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "IpAddress", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibb52TestProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 56))
mibb52TestProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 56, 1), )
if mibBuilder.loadTexts: mibb52TestProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibb52TestProfileTable.setDescription('A list of mibb52TestProfile profile entries.')
mibb52TestProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1), ).setIndexNames((0, "ASCEND-MIBB52TEST-MIB", "b52TestProfile-Index-o"))
if mibBuilder.loadTexts: mibb52TestProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibb52TestProfileEntry.setDescription('A mibb52TestProfile entry containing objects that maps to the parameters of mibb52TestProfile profile.')
b52TestProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 1), Integer32()).setLabel("b52TestProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: b52TestProfile_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: b52TestProfile_Index_o.setDescription('')
b52TestProfile_TftpBootType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("tftpBootFirst", 2), ("tftpBootSecond", 3)))).setLabel("b52TestProfile-TftpBootType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: b52TestProfile_TftpBootType.setStatus('mandatory')
if mibBuilder.loadTexts: b52TestProfile_TftpBootType.setDescription('TFTP Boot type')
b52TestProfile_TftpBootHostName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 3), DisplayString()).setLabel("b52TestProfile-TftpBootHostName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: b52TestProfile_TftpBootHostName.setStatus('mandatory')
if mibBuilder.loadTexts: b52TestProfile_TftpBootHostName.setDescription('Name of the TFTP boot server we should use.')
b52TestProfile_TftpBootBaseName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 4), DisplayString()).setLabel("b52TestProfile-TftpBootBaseName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: b52TestProfile_TftpBootBaseName.setStatus('mandatory')
if mibBuilder.loadTexts: b52TestProfile_TftpBootBaseName.setDescription('Base filename for the TFTP boot files we should use.')
b52TestProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("b52TestProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: b52TestProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: b52TestProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBB52TEST-MIB", DisplayString=DisplayString, b52TestProfile_TftpBootBaseName=b52TestProfile_TftpBootBaseName, b52TestProfile_Action_o=b52TestProfile_Action_o, b52TestProfile_TftpBootHostName=b52TestProfile_TftpBootHostName, mibb52TestProfile=mibb52TestProfile, b52TestProfile_TftpBootType=b52TestProfile_TftpBootType, mibb52TestProfileEntry=mibb52TestProfileEntry, mibb52TestProfileTable=mibb52TestProfileTable, b52TestProfile_Index_o=b52TestProfile_Index_o)
