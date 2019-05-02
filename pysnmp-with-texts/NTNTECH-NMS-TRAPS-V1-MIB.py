#
# PySNMP MIB module NTNTECH-NMS-TRAPS-V1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTNTECH-NMS-TRAPS-V1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
mumStaFanState, = mibBuilder.importSymbols("NTNTECH-CHASSIS-STATUS-MIB", "mumStaFanState")
ifStaSlotIndex, ifStaType = mibBuilder.importSymbols("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex", "ifStaType")
ntntechNMSTraps, = mibBuilder.importSymbols("NTNTECH-ROOT-MIB", "ntntechNMSTraps")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, iso, MibIdentifier, Gauge32, ModuleIdentity, Unsigned32, TimeTicks, Counter64, Counter32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "iso", "MibIdentifier", "Gauge32", "ModuleIdentity", "Unsigned32", "TimeTicks", "Counter64", "Counter32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
envFanTrap_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,1001)).setLabel("envFanTrap-v1").setObjects(("NTNTECH-CHASSIS-STATUS-MIB", "mumStaFanState"))
if mibBuilder.loadTexts: envFanTrap_v1.setDescription('There has been a change in the Fan state.')
envTempNormal_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,1002)).setLabel("envTempNormal-v1")
if mibBuilder.loadTexts: envTempNormal_v1.setDescription('The normal operating temperature inside the chassis has returned. Note: This trap applies to the micro DSLAMs only.')
envTempExceeded_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,1003)).setLabel("envTempExceeded-v1")
if mibBuilder.loadTexts: envTempExceeded_v1.setDescription('The normal operating temperature inside the chassis has been exceeded. Note: This trap applies to the micro DSLAMs only.')
invIfModPresentTrap_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,2001)).setLabel("invIfModPresentTrap-v1").setObjects(("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex"), ("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType"))
if mibBuilder.loadTexts: invIfModPresentTrap_v1.setDescription("A change was detected related to the population state of a chassis slot. This trap will be triggered when the population state of a slot makes the transition from vacant to present, where present is any valid interface module type as defined by 'ifStaType'.")
invIfModRemovedTrap_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,2002)).setLabel("invIfModRemovedTrap-v1").setObjects(("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex"), ("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType"))
if mibBuilder.loadTexts: invIfModRemovedTrap_v1.setDescription("A change was detected related to the population state of a chassis slot. This trap will be triggered when the population state of a slot makes the transition from present, to vacant. In otherwords, this trap will be triggered if an interface module of type 'a' is immediately replaced with one of type 'b' or 40 seconds after an interface module is removed leaving the slot vacant.")
mibBuilder.exportSymbols("NTNTECH-NMS-TRAPS-V1-MIB", invIfModPresentTrap_v1=invIfModPresentTrap_v1, invIfModRemovedTrap_v1=invIfModRemovedTrap_v1, envTempNormal_v1=envTempNormal_v1, envTempExceeded_v1=envTempExceeded_v1, envFanTrap_v1=envFanTrap_v1)
