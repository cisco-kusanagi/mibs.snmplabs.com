#
# PySNMP MIB module TUBS-IBR-LINUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-IBR-LINUX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, TimeTicks, Counter64, ModuleIdentity, NotificationType, Unsigned32, Gauge32, IpAddress, iso, Bits, ObjectIdentity, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Counter64", "ModuleIdentity", "NotificationType", "Unsigned32", "Gauge32", "IpAddress", "iso", "Bits", "ObjectIdentity", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibr, = mibBuilder.importSymbols("TUBS-REGISTRATION", "ibr")
linuxMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 5))
linuxMIB.setRevisions(('1998-01-07 06:22', '1997-02-14 10:23', '1994-11-15 20:24',))
if mibBuilder.loadTexts: linuxMIB.setLastUpdated('9801070622Z')
if mibBuilder.loadTexts: linuxMIB.setOrganization('TU Braunschweig')
linuxObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2))
linuxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3))
class LoadValue(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

linuxCPU = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxCPU.setStatus('current')
linuxBogo = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxBogo.setStatus('current')
linuxLoadAvg1 = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 3), LoadValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxLoadAvg1.setStatus('current')
linuxLoadAvg5 = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 4), LoadValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxLoadAvg5.setStatus('current')
linuxLoadAvg15 = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 5), LoadValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxLoadAvg15.setStatus('current')
linuxCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 1))
linuxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 2))
linuxCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 1, 1)).setObjects(("TUBS-IBR-LINUX-MIB", "linuxGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linuxCompliance = linuxCompliance.setStatus('current')
linuxGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 2, 1)).setObjects(("TUBS-IBR-LINUX-MIB", "linuxCPU"), ("TUBS-IBR-LINUX-MIB", "linuxBogo"), ("TUBS-IBR-LINUX-MIB", "linuxLoadAvg1"), ("TUBS-IBR-LINUX-MIB", "linuxLoadAvg5"), ("TUBS-IBR-LINUX-MIB", "linuxLoadAvg15"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linuxGroup = linuxGroup.setStatus('current')
mibBuilder.exportSymbols("TUBS-IBR-LINUX-MIB", linuxCPU=linuxCPU, linuxConformance=linuxConformance, linuxCompliances=linuxCompliances, linuxGroups=linuxGroups, PYSNMP_MODULE_ID=linuxMIB, linuxLoadAvg5=linuxLoadAvg5, linuxCompliance=linuxCompliance, linuxGroup=linuxGroup, linuxObjects=linuxObjects, linuxMIB=linuxMIB, linuxLoadAvg15=linuxLoadAvg15, LoadValue=LoadValue, linuxBogo=linuxBogo, linuxLoadAvg1=linuxLoadAvg1)
