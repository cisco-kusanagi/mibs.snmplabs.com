#
# PySNMP MIB module CISCO-MEDIA-GATEWAY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MEDIA-GATEWAY-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:49:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Unsigned32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Gauge32, Bits, ObjectIdentity, IpAddress, Counter64, Counter32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Gauge32", "Bits", "ObjectIdentity", "IpAddress", "Counter64", "Counter32", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMediaGatewayCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 375))
ciscoMediaGatewayCapability.setRevisions(('2004-02-05 00:00',))
if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setLastUpdated('200402050000Z')
if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setOrganization('Cisco Systems, Inc.')
cMediaGatewayCapV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 375, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMediaGatewayCapV5R00 = cMediaGatewayCapV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMediaGatewayCapV5R00 = cMediaGatewayCapV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-MEDIA-GATEWAY-CAPABILITY", cMediaGatewayCapV5R00=cMediaGatewayCapV5R00, ciscoMediaGatewayCapability=ciscoMediaGatewayCapability, PYSNMP_MODULE_ID=ciscoMediaGatewayCapability)
