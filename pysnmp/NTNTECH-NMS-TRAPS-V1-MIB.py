#
# PySNMP MIB module NTNTECH-NMS-TRAPS-V1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTNTECH-NMS-TRAPS-V1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
mumStaFanState, = mibBuilder.importSymbols("NTNTECH-CHASSIS-STATUS-MIB", "mumStaFanState")
ifStaType, ifStaSlotIndex = mibBuilder.importSymbols("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType", "ifStaSlotIndex")
ntntechNMSTraps, = mibBuilder.importSymbols("NTNTECH-ROOT-MIB", "ntntechNMSTraps")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, iso, TimeTicks, Counter64, IpAddress, Integer32, Unsigned32, Gauge32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "iso", "TimeTicks", "Counter64", "IpAddress", "Integer32", "Unsigned32", "Gauge32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
envFanTrap_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,1001)).setLabel("envFanTrap-v1").setObjects(("NTNTECH-CHASSIS-STATUS-MIB", "mumStaFanState"))
envTempNormal_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,1002)).setLabel("envTempNormal-v1")
envTempExceeded_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,1003)).setLabel("envTempExceeded-v1")
invIfModPresentTrap_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,2001)).setLabel("invIfModPresentTrap-v1").setObjects(("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex"), ("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType"))
invIfModRemovedTrap_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,2002)).setLabel("invIfModRemovedTrap-v1").setObjects(("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex"), ("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType"))
mibBuilder.exportSymbols("NTNTECH-NMS-TRAPS-V1-MIB", invIfModPresentTrap_v1=invIfModPresentTrap_v1, envTempNormal_v1=envTempNormal_v1, invIfModRemovedTrap_v1=invIfModRemovedTrap_v1, envTempExceeded_v1=envTempExceeded_v1, envFanTrap_v1=envFanTrap_v1)
