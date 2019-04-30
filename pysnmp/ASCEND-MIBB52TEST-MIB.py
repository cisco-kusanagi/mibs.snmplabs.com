#
# PySNMP MIB module ASCEND-MIBB52TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBB52TEST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, iso, ObjectIdentity, NotificationType, MibIdentifier, Gauge32, Counter64, Unsigned32, TimeTicks, IpAddress, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "iso", "ObjectIdentity", "NotificationType", "MibIdentifier", "Gauge32", "Counter64", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibb52TestProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 56))
mibb52TestProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 56, 1), )
if mibBuilder.loadTexts: mibb52TestProfileTable.setStatus('mandatory')
mibb52TestProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1), ).setIndexNames((0, "ASCEND-MIBB52TEST-MIB", "b52TestProfile-Index-o"))
if mibBuilder.loadTexts: mibb52TestProfileEntry.setStatus('mandatory')
b52TestProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 1), Integer32()).setLabel("b52TestProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: b52TestProfile_Index_o.setStatus('mandatory')
b52TestProfile_TftpBootType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("tftpBootFirst", 2), ("tftpBootSecond", 3)))).setLabel("b52TestProfile-TftpBootType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: b52TestProfile_TftpBootType.setStatus('mandatory')
b52TestProfile_TftpBootHostName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 3), DisplayString()).setLabel("b52TestProfile-TftpBootHostName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: b52TestProfile_TftpBootHostName.setStatus('mandatory')
b52TestProfile_TftpBootBaseName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 4), DisplayString()).setLabel("b52TestProfile-TftpBootBaseName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: b52TestProfile_TftpBootBaseName.setStatus('mandatory')
b52TestProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("b52TestProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: b52TestProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBB52TEST-MIB", b52TestProfile_TftpBootHostName=b52TestProfile_TftpBootHostName, b52TestProfile_TftpBootBaseName=b52TestProfile_TftpBootBaseName, b52TestProfile_Index_o=b52TestProfile_Index_o, mibb52TestProfile=mibb52TestProfile, b52TestProfile_TftpBootType=b52TestProfile_TftpBootType, mibb52TestProfileTable=mibb52TestProfileTable, mibb52TestProfileEntry=mibb52TestProfileEntry, b52TestProfile_Action_o=b52TestProfile_Action_o, DisplayString=DisplayString)
