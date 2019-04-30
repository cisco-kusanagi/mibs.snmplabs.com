#
# PySNMP MIB module CABLETRON-TRAPS-IRM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CABLETRON-TRAPS-IRM
# Produced by pysmi-0.3.4 at Mon Apr 29 17:26:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
boardIndex, boardSrcAddrLocked = mibBuilder.importSymbols("IRM3-MIB", "boardIndex", "boardSrcAddrLocked")
deviceSrcAddrLocked, devTrafficThreshold, devErrorThreshold, devCollsThreshold, devErrorSource, devBroadThreshold, deviceTimeBase = mibBuilder.importSymbols("REPEATER-MIB-2", "deviceSrcAddrLocked", "devTrafficThreshold", "devErrorThreshold", "devCollsThreshold", "devErrorSource", "devBroadThreshold", "deviceTimeBase")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, enterprises, Integer32, NotificationType, Unsigned32, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "enterprises", "Integer32", "NotificationType", "Unsigned32", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
srcAddressPortGrpLockStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 52) + (0,308)).setObjects(("IRM3-MIB", "boardIndex"), ("IRM3-MIB", "boardSrcAddrLocked"))
deviceTrafficThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52) + (0,268)).setObjects(("REPEATER-MIB-2", "devTrafficThreshold"), ("REPEATER-MIB-2", "deviceTimeBase"))
deviceErrorThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52) + (0,269)).setObjects(("REPEATER-MIB-2", "devErrorThreshold"), ("REPEATER-MIB-2", "devErrorSource"), ("REPEATER-MIB-2", "deviceTimeBase"))
deviceCollsionThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52) + (0,270)).setObjects(("REPEATER-MIB-2", "devCollsThreshold"), ("REPEATER-MIB-2", "deviceTimeBase"))
deviceBroadcastThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52) + (0,288)).setObjects(("REPEATER-MIB-2", "devBroadThreshold"), ("REPEATER-MIB-2", "deviceTimeBase"))
lockStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 52) + (0,278)).setObjects(("REPEATER-MIB-2", "deviceSrcAddrLocked"))
mibBuilder.exportSymbols("CABLETRON-TRAPS-IRM", srcAddressPortGrpLockStatusChange=srcAddressPortGrpLockStatusChange, deviceCollsionThresholdExceeded=deviceCollsionThresholdExceeded, lockStatusChanged=lockStatusChanged, deviceErrorThresholdExceeded=deviceErrorThresholdExceeded, deviceTrafficThresholdExceeded=deviceTrafficThresholdExceeded, cabletron=cabletron, deviceBroadcastThresholdExceeded=deviceBroadcastThresholdExceeded)
