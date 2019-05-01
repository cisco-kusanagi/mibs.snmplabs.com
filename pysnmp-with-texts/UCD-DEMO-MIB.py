#
# PySNMP MIB module UCD-DEMO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UCD-DEMO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:28:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter32, NotificationType, MibIdentifier, Integer32, Gauge32, TimeTicks, Counter64, Bits, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "NotificationType", "MibIdentifier", "Integer32", "Gauge32", "TimeTicks", "Counter64", "Bits", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ucdavis, = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdavis")
ucdDemoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021, 14))
ucdDemoMIB.setRevisions(('1999-12-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ucdDemoMIB.setRevisionsDescriptions(('SMIv2 version converted from older MIB definitions.',))
if mibBuilder.loadTexts: ucdDemoMIB.setLastUpdated('9912090000Z')
if mibBuilder.loadTexts: ucdDemoMIB.setOrganization('University of California, Davis')
if mibBuilder.loadTexts: ucdDemoMIB.setContactInfo('This mib is no longer being maintained by the University of California and is now in life-support-mode and being maintained by the net-snmp project. The best place to write for public questions about the net-snmp-coders mailing list at net-snmp-coders@lists.sourceforge.net. postal: Wes Hardaker P.O. Box 382 Davis CA 95617 email: net-snmp-coders@lists.sourceforge.net ')
if mibBuilder.loadTexts: ucdDemoMIB.setDescription('The UCD-SNMP Demonstration MIB.')
ucdDemoMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 14, 1))
ucdDemoPublic = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1))
ucdDemoResetKeys = MibScalar((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ucdDemoResetKeys.setStatus('current')
if mibBuilder.loadTexts: ucdDemoResetKeys.setDescription("A set of value 1 to this object resets the demonstration user's auth and priv keys to the keys based on the P->Ku->Kul transformation of the value of the ucdDemoPasspharse object. Values other than 1 are ignored.")
ucdDemoPublicString = MibScalar((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ucdDemoPublicString.setStatus('current')
if mibBuilder.loadTexts: ucdDemoPublicString.setDescription('A publicly settable string that can be set for testing snmpsets. This value has no real usage other than testing purposes.')
ucdDemoUserList = MibScalar((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ucdDemoUserList.setStatus('current')
if mibBuilder.loadTexts: ucdDemoUserList.setDescription('The list of users affected by the ucdDemoResetKeys object.')
ucdDemoPassphrase = MibScalar((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ucdDemoPassphrase.setStatus('current')
if mibBuilder.loadTexts: ucdDemoPassphrase.setDescription('The demo passphrase that ucdDemoResetKeys changes each users localized key to based on the P->Ku->Kul transformation.')
mibBuilder.exportSymbols("UCD-DEMO-MIB", ucdDemoResetKeys=ucdDemoResetKeys, ucdDemoPassphrase=ucdDemoPassphrase, PYSNMP_MODULE_ID=ucdDemoMIB, ucdDemoMIBObjects=ucdDemoMIBObjects, ucdDemoMIB=ucdDemoMIB, ucdDemoUserList=ucdDemoUserList, ucdDemoPublicString=ucdDemoPublicString, ucdDemoPublic=ucdDemoPublic)
