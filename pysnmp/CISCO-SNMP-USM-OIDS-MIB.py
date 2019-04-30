#
# PySNMP MIB module CISCO-SNMP-USM-OIDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-USM-OIDS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, Unsigned32, TimeTicks, Integer32, Counter64, Bits, Gauge32, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Unsigned32", "TimeTicks", "Integer32", "Counter64", "Bits", "Gauge32", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpUsmOidsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 6))
ciscoSnmpUsmOidsMIB.setRevisions(('2006-02-28 00:00',))
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setLastUpdated('200602280000Z')
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setOrganization('Cisco Systems, Inc.')
ciscoSnmpPrivProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1))
cusmAESCfb192PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 1))
cusmAESCfb256PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 2))
cusm3DES168PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 3))
mibBuilder.exportSymbols("CISCO-SNMP-USM-OIDS-MIB", cusmAESCfb192PrivProtocol=cusmAESCfb192PrivProtocol, ciscoSnmpUsmOidsMIB=ciscoSnmpUsmOidsMIB, ciscoSnmpPrivProtocols=ciscoSnmpPrivProtocols, cusmAESCfb256PrivProtocol=cusmAESCfb256PrivProtocol, PYSNMP_MODULE_ID=ciscoSnmpUsmOidsMIB, cusm3DES168PrivProtocol=cusm3DES168PrivProtocol)
