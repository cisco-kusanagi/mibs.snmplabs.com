#
# PySNMP MIB module FORTINET-FORTIMANAGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FORTINET-FORTIMANAGER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:00:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
fortinet, fnSysSerial = mibBuilder.importSymbols("FORTINET-CORE-MIB", "fortinet", "fnSysSerial")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
iso, MibIdentifier, IpAddress, Unsigned32, Bits, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "IpAddress", "Unsigned32", "Bits", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fnFortiManagerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 12356, 103))
fnFortiManagerMib.setRevisions(('2008-07-18 00:00', '2008-06-26 00:00', '2008-06-16 00:00', '2008-06-10 00:00',))
if mibBuilder.loadTexts: fnFortiManagerMib.setLastUpdated('200807180000Z')
if mibBuilder.loadTexts: fnFortiManagerMib.setOrganization('Fortinet Technologies, Inc.')
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
fmTrapsComplianceGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12356, 103, 10, 1)).setObjects(("FORTINET-FORTIMANAGER-MIB", "fmTrapHASwitch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmTrapsComplianceGroup = fmTrapsComplianceGroup.setStatus('current')
fmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12356, 103, 10, 100)).setObjects(("FORTINET-FORTIMANAGER-MIB", "fmTrapsComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmMIBCompliance = fmMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("FORTINET-FORTIMANAGER-MIB", fmTrapPrefix=fmTrapPrefix, fmg100=fmg100, fmg2000XL=fmg2000XL, fmTrapsComplianceGroup=fmTrapsComplianceGroup, fnFortiManagerMib=fnFortiManagerMib, fmTrapObject=fmTrapObject, fmg3000=fmg3000, fmMIBConformance=fmMIBConformance, fmMIBCompliance=fmMIBCompliance, fmg400=fmg400, fmTrapHASwitch=fmTrapHASwitch, fmg400A=fmg400A, fmTraps=fmTraps, fmg3000B=fmg3000B, PYSNMP_MODULE_ID=fnFortiManagerMib, fmModel=fmModel)
