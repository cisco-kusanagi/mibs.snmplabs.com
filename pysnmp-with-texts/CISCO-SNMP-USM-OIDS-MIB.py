#
# PySNMP MIB module CISCO-SNMP-USM-OIDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-USM-OIDS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:12:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, Gauge32, ModuleIdentity, NotificationType, MibIdentifier, IpAddress, Bits, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "Gauge32", "ModuleIdentity", "NotificationType", "MibIdentifier", "IpAddress", "Bits", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSnmpUsmOidsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 6))
ciscoSnmpUsmOidsMIB.setRevisions(('2006-02-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setLastUpdated('200602280000Z')
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setDescription("This MIB extends the OID's for SNMP-USM-MIB specified in RFC 3414. The privacy protocol OID's specified herein are intended to be used as values for usmUserPrivProtocol when managing SNMPv3 users via the snmpUsmMIB. This MIB defines the OID's for the following encryption options: * 192 bit key size AES * 256 bit key size AES * 168 bit key size 3DES. OID for 128 bit key size AES encryption is defined in SNMP-USM-AES-MIB as per the RFC 3826.")
ciscoSnmpPrivProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1))
cusmAESCfb192PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 1))
cusmAESCfb256PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 2))
cusm3DES168PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 3))
mibBuilder.exportSymbols("CISCO-SNMP-USM-OIDS-MIB", ciscoSnmpPrivProtocols=ciscoSnmpPrivProtocols, cusmAESCfb192PrivProtocol=cusmAESCfb192PrivProtocol, cusmAESCfb256PrivProtocol=cusmAESCfb256PrivProtocol, PYSNMP_MODULE_ID=ciscoSnmpUsmOidsMIB, ciscoSnmpUsmOidsMIB=ciscoSnmpUsmOidsMIB, cusm3DES168PrivProtocol=cusm3DES168PrivProtocol)
