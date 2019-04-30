#
# PySNMP MIB module OBSERVIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OBSERVIUM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:22:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
TimeTicks, MibIdentifier, Counter64, Gauge32, enterprises, ModuleIdentity, mib_2, ObjectIdentity, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, IpAddress, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Counter64", "Gauge32", "enterprises", "ModuleIdentity", "mib-2", "ObjectIdentity", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "IpAddress", "Unsigned32", "NotificationType")
TruthValue, TestAndIncr, PhysAddress, TextualConvention, RowStatus, TimeStamp, DisplayString, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TestAndIncr", "PhysAddress", "TextualConvention", "RowStatus", "TimeStamp", "DisplayString", "AutonomousType")
observium = MibIdentifier((1, 3, 6, 1, 4, 1, 36602))
obsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 36602, 1))
obsHostInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36602, 1, 1))
obsLinuxDistro = MibScalar((1, 3, 6, 1, 4, 1, 36602, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obsLinuxDistro.setStatus('current')
obsCPUUsage = MibScalar((1, 3, 6, 1, 4, 1, 36602, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: obsCPUUsage.setStatus('mandatory')
mibBuilder.exportSymbols("OBSERVIUM-MIB", obsHostInfo=obsHostInfo, observium=observium, obsCPUUsage=obsCPUUsage, obsObjects=obsObjects, obsLinuxDistro=obsLinuxDistro)
