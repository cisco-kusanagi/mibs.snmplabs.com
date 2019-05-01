#
# PySNMP MIB module CISCO-MEDIA-GATEWAY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MEDIA-GATEWAY-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:06:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, Integer32, ModuleIdentity, NotificationType, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, ObjectIdentity, TimeTicks, Counter32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "ModuleIdentity", "NotificationType", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "ObjectIdentity", "TimeTicks", "Counter32", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMediaGatewayCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 375))
ciscoMediaGatewayCapability.setRevisions(('2004-02-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setLastUpdated('200402050000Z')
if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setDescription('The agent capabilities for CISCO-MEDIA-GATEWAY-MIB.')
cMediaGatewayCapV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 375, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMediaGatewayCapV5R00 = cMediaGatewayCapV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMediaGatewayCapV5R00 = cMediaGatewayCapV5R00.setStatus('current')
if mibBuilder.loadTexts: cMediaGatewayCapV5R00.setDescription('Agent capabilities for VXSM in Release 5.0.0.')
mibBuilder.exportSymbols("CISCO-MEDIA-GATEWAY-CAPABILITY", PYSNMP_MODULE_ID=ciscoMediaGatewayCapability, ciscoMediaGatewayCapability=ciscoMediaGatewayCapability, cMediaGatewayCapV5R00=cMediaGatewayCapV5R00)
