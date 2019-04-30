#
# PySNMP MIB module NORTEL-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NORTEL-GENERIC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:14:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
nortel, = mibBuilder.importSymbols("NORTEL-MIB", "nortel")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Gauge32, ModuleIdentity, Counter64, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Integer32, MibIdentifier, Counter32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "ModuleIdentity", "Counter64", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Integer32", "MibIdentifier", "Counter32", "IpAddress", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nortelGenericMIBs = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 29))
nortelGenericMIBs.setRevisions(('1999-06-24 00:00', '1999-05-31 00:00', '1999-04-12 00:00', '1999-03-22 00:00',))
if mibBuilder.loadTexts: nortelGenericMIBs.setLastUpdated('9906240000Z')
if mibBuilder.loadTexts: nortelGenericMIBs.setOrganization('Nortel Networks')
nortelNetworkManagementInterfaceMIBs = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1))
if mibBuilder.loadTexts: nortelNetworkManagementInterfaceMIBs.setStatus('current')
mibBuilder.exportSymbols("NORTEL-GENERIC-MIB", nortelNetworkManagementInterfaceMIBs=nortelNetworkManagementInterfaceMIBs, PYSNMP_MODULE_ID=nortelGenericMIBs, nortelGenericMIBs=nortelGenericMIBs)
