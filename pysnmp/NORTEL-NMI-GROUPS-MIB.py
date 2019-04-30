#
# PySNMP MIB module NORTEL-NMI-GROUPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NORTEL-NMI-GROUPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:14:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
nortelNMIconformanceMIBs, = mibBuilder.importSymbols("NORTEL-NMI-CONFORMANCE-MIB", "nortelNMIconformanceMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, TimeTicks, Gauge32, Unsigned32, NotificationType, ModuleIdentity, Counter64, Counter32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Gauge32", "Unsigned32", "NotificationType", "ModuleIdentity", "Counter64", "Counter32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nortelNMImibGroups = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1))
nortelNMImibGroups.setRevisions(('1999-06-24 00:00',))
if mibBuilder.loadTexts: nortelNMImibGroups.setLastUpdated('9906240000Z')
if mibBuilder.loadTexts: nortelNMImibGroups.setOrganization('Nortel Networks')
nortelNMIobjectGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 1))
if mibBuilder.loadTexts: nortelNMIobjectGroups.setStatus('current')
nortelNMInotificationGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 2))
if mibBuilder.loadTexts: nortelNMInotificationGroups.setStatus('current')
mibBuilder.exportSymbols("NORTEL-NMI-GROUPS-MIB", nortelNMImibGroups=nortelNMImibGroups, nortelNMIobjectGroups=nortelNMIobjectGroups, nortelNMInotificationGroups=nortelNMInotificationGroups, PYSNMP_MODULE_ID=nortelNMImibGroups)
