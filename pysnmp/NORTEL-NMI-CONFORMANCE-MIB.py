#
# PySNMP MIB module NORTEL-NMI-CONFORMANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NORTEL-NMI-CONFORMANCE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:14:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
nortelNetworkManagementInterfaceMIBs, = mibBuilder.importSymbols("NORTEL-GENERIC-MIB", "nortelNetworkManagementInterfaceMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Gauge32, ObjectIdentity, Unsigned32, NotificationType, ModuleIdentity, Counter64, Counter32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "ModuleIdentity", "Counter64", "Counter32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nortelNMIconformanceMIBs = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 2))
nortelNMIconformanceMIBs.setRevisions(('1999-06-24 00:00', '1999-05-31 00:00',))
if mibBuilder.loadTexts: nortelNMIconformanceMIBs.setLastUpdated('9906240000Z')
if mibBuilder.loadTexts: nortelNMIconformanceMIBs.setOrganization('Nortel Networks')
mibBuilder.exportSymbols("NORTEL-NMI-CONFORMANCE-MIB", PYSNMP_MODULE_ID=nortelNMIconformanceMIBs, nortelNMIconformanceMIBs=nortelNMIconformanceMIBs)
