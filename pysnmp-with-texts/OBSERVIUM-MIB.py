#
# PySNMP MIB module OBSERVIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OBSERVIUM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:32:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
Counter32, ObjectIdentity, enterprises, Counter64, NotificationType, IpAddress, MibIdentifier, Integer32, ModuleIdentity, TimeTicks, mib_2, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "enterprises", "Counter64", "NotificationType", "IpAddress", "MibIdentifier", "Integer32", "ModuleIdentity", "TimeTicks", "mib-2", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32")
DisplayString, PhysAddress, RowStatus, TestAndIncr, AutonomousType, TimeStamp, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "RowStatus", "TestAndIncr", "AutonomousType", "TimeStamp", "TextualConvention", "TruthValue")
observium = MibIdentifier((1, 3, 6, 1, 4, 1, 36602))
obsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 36602, 1))
obsHostInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36602, 1, 1))
obsLinuxDistro = MibScalar((1, 3, 6, 1, 4, 1, 36602, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obsLinuxDistro.setStatus('current')
if mibBuilder.loadTexts: obsLinuxDistro.setDescription('Linux distribution and version')
obsCPUUsage = MibScalar((1, 3, 6, 1, 4, 1, 36602, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: obsCPUUsage.setStatus('mandatory')
if mibBuilder.loadTexts: obsCPUUsage.setDescription('CPU Usage')
mibBuilder.exportSymbols("OBSERVIUM-MIB", obsLinuxDistro=obsLinuxDistro, observium=observium, obsHostInfo=obsHostInfo, obsCPUUsage=obsCPUUsage, obsObjects=obsObjects)
