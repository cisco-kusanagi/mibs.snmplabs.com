#
# PySNMP MIB module CISCO-DOT11-CONTEXT-SERVICES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-CONTEXT-SERVICES-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:55:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Unsigned32, Integer32, Bits, iso, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, ObjectIdentity, MibIdentifier, IpAddress, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "Bits", "iso", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cDot11ContextServicesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 347))
if mibBuilder.loadTexts: cDot11ContextServicesCapability.setLastUpdated('200309170000Z')
if mibBuilder.loadTexts: cDot11ContextServicesCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cDot11ContextServicesCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: cDot11ContextServicesCapability.setDescription('Agent capabilities for CISCO-DOT11-CONTEXT-SERVICES-MIB')
cDot11ContextServicesCapabilityV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 347, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11ContextServicesCapabilityV1 = cDot11ContextServicesCapabilityV1.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11ContextServicesCapabilityV1 = cDot11ContextServicesCapabilityV1.setStatus('current')
if mibBuilder.loadTexts: cDot11ContextServicesCapabilityV1.setDescription('Cisco Context Services MIB capabilities')
mibBuilder.exportSymbols("CISCO-DOT11-CONTEXT-SERVICES-CAPABILITY", PYSNMP_MODULE_ID=cDot11ContextServicesCapability, cDot11ContextServicesCapabilityV1=cDot11ContextServicesCapabilityV1, cDot11ContextServicesCapability=cDot11ContextServicesCapability)
