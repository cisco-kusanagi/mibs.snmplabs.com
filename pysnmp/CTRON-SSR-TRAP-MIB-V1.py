#
# PySNMP MIB module CTRON-SSR-TRAP-MIB-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-SSR-TRAP-MIB-V1
# Produced by pysmi-0.3.4 at Mon Apr 29 18:16:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
sysHwFan, sysHwTemperature, sysHwModuleSlotNumber, sysHwPowerSupply = mibBuilder.importSymbols("CTRON-SSR-HARDWARE-MIB", "sysHwFan", "sysHwTemperature", "sysHwModuleSlotNumber", "sysHwPowerSupply")
ssrTraps, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrTraps")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, NotificationType, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Integer32, IpAddress, Unsigned32, ObjectIdentity, Bits, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "NotificationType", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Integer32", "IpAddress", "Unsigned32", "ObjectIdentity", "Bits", "MibIdentifier", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
envPowerSupplyFailed = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,1)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"))
envPowerSupplyRecovered = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,2)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"))
envFanFailed = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,3)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwFan"))
envFanRecovered = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,4)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwFan"))
envTempExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,5)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"))
envTempNormal = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,6)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"))
envHotSwapIn = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,7)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
envHotSwapOut = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,8)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
envBackupControlModuleOnline = NotificationType((1, 3, 6, 1, 4, 1, 52, 2501, 10) + (0,9)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
mibBuilder.exportSymbols("CTRON-SSR-TRAP-MIB-V1", envPowerSupplyFailed=envPowerSupplyFailed, envBackupControlModuleOnline=envBackupControlModuleOnline, envPowerSupplyRecovered=envPowerSupplyRecovered, envHotSwapOut=envHotSwapOut, envTempExceeded=envTempExceeded, envTempNormal=envTempNormal, envHotSwapIn=envHotSwapIn, envFanFailed=envFanFailed, envFanRecovered=envFanRecovered)
