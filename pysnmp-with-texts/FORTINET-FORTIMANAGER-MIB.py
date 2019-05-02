#
# PySNMP MIB module FORTINET-FORTIMANAGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FORTINET-FORTIMANAGER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:14:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
fnSysSerial, fortinet = mibBuilder.importSymbols("FORTINET-CORE-MIB", "fnSysSerial", "fortinet")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
iso, Unsigned32, Bits, Integer32, MibIdentifier, ModuleIdentity, Counter64, TimeTicks, NotificationType, Gauge32, ObjectIdentity, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Bits", "Integer32", "MibIdentifier", "ModuleIdentity", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "ObjectIdentity", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fnFortiManagerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 12356, 103))
fnFortiManagerMib.setRevisions(('2008-07-18 00:00', '2008-06-26 00:00', '2008-06-16 00:00', '2008-06-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fnFortiManagerMib.setRevisionsDescriptions(('Add sysName to fmTrapHASwitch.', 'OID correction for fnFortiManagerMib.', 'Spelling corrections.', 'Initial version of FORTINET-FORTIMANAGER-MIB.',))
if mibBuilder.loadTexts: fnFortiManagerMib.setLastUpdated('200807180000Z')
if mibBuilder.loadTexts: fnFortiManagerMib.setOrganization('Fortinet Technologies, Inc.')
if mibBuilder.loadTexts: fnFortiManagerMib.setContactInfo(' Technical Support email: support@fortinet.com http://www.fortinet.com')
if mibBuilder.loadTexts: fnFortiManagerMib.setDescription('MIB module for Fortinet FortiManager devices.')
fmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 0))
fmTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 0, 0))
fmTrapObject = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 0, 1))
fmModel = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1))
fmg100 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1, 1000))
fmg400 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1, 4000))
fmg400A = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1, 4001))
fmg2000XL = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1, 20000))
fmg3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1, 30000))
fmg3000B = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 1, 30002))
fmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 103, 10))
fmTrapHASwitch = NotificationType((1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 401)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fmTrapHASwitch.setStatus('current')
if mibBuilder.loadTexts: fmTrapHASwitch.setDescription('FortiManager HA cluster has been re-arranged. A new master has been selected and asserted.')
fmTrapsComplianceGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12356, 103, 10, 1)).setObjects(("FORTINET-FORTIMANAGER-MIB", "fmTrapHASwitch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmTrapsComplianceGroup = fmTrapsComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: fmTrapsComplianceGroup.setDescription('Event notifications')
fmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12356, 103, 10, 100)).setObjects(("FORTINET-FORTIMANAGER-MIB", "fmTrapsComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmMIBCompliance = fmMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: fmMIBCompliance.setDescription('The compliance statement for the FortiManager MIB.')
mibBuilder.exportSymbols("FORTINET-FORTIMANAGER-MIB", fmg3000=fmg3000, fmg2000XL=fmg2000XL, fmTrapObject=fmTrapObject, fmTrapsComplianceGroup=fmTrapsComplianceGroup, fmg100=fmg100, fmModel=fmModel, fmg400A=fmg400A, fmMIBConformance=fmMIBConformance, fmTrapHASwitch=fmTrapHASwitch, PYSNMP_MODULE_ID=fnFortiManagerMib, fmg400=fmg400, fnFortiManagerMib=fnFortiManagerMib, fmTrapPrefix=fmTrapPrefix, fmMIBCompliance=fmMIBCompliance, fmTraps=fmTraps, fmg3000B=fmg3000B)
