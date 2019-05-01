#
# PySNMP MIB module RDN-SMSTraps-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-SMSTraps-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
docsIfCmtsCmStatusValue, docsIfCmtsCmStatusMacAddress = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusValue", "docsIfCmtsCmStatusMacAddress")
riverdelta, = mibBuilder.importSymbols("RDN-MIB", "riverdelta")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, enterprises, Gauge32, Unsigned32, Integer32, NotificationType, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, ObjectIdentity, NotificationType, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "enterprises", "Gauge32", "Unsigned32", "Integer32", "NotificationType", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "ObjectIdentity", "NotificationType", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnSubscriberTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 5))
rdnCableModemV1Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 5, 1))
rdnCableModemStatusV1 = NotificationType((1, 3, 6, 1, 4, 1, 4981) + (0,1)).setObjects(("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusValue"))
if mibBuilder.loadTexts: rdnCableModemStatusV1.setDescription('The event is generated when the SRM receives a valid DHCP PACK packet. ')
rdnCableModemV2Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 5, 2))
rdnCableModemStatusV2 = NotificationType((1, 3, 6, 1, 4, 1, 4981, 5, 2, 1)).setObjects(("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusValue"))
if mibBuilder.loadTexts: rdnCableModemStatusV2.setStatus('current')
if mibBuilder.loadTexts: rdnCableModemStatusV2.setDescription('The CM trap signifies that the SNMPv2 entity in the device acting in an agent role has detected a cable modem registration event based on a valid DHCP PACK packet being sent to the CM.')
mibBuilder.exportSymbols("RDN-SMSTraps-MIB", rdnCableModemV1Traps=rdnCableModemV1Traps, rdnCableModemStatusV1=rdnCableModemStatusV1, rdnSubscriberTraps=rdnSubscriberTraps, rdnCableModemV2Traps=rdnCableModemV2Traps, rdnCableModemStatusV2=rdnCableModemStatusV2)
