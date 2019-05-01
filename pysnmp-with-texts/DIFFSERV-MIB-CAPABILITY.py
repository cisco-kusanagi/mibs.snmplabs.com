#
# PySNMP MIB module DIFFSERV-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DIFFSERV-MIB-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:47:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
IndexInteger, IfDirection = mibBuilder.importSymbols("DIFFSERV-MIB", "IndexInteger", "IfDirection")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ObjectIdentity, MibIdentifier, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, ModuleIdentity, NotificationType, Gauge32, Unsigned32, Counter64, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "ModuleIdentity", "NotificationType", "Gauge32", "Unsigned32", "Counter64", "iso", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
diffServMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 377))
diffServMibCapability.setRevisions(('2003-10-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: diffServMibCapability.setRevisionsDescriptions(('The capabilities description of DIFFSERV-MIB (RFC 3289) for MDS 1.3(1).',))
if mibBuilder.loadTexts: diffServMibCapability.setLastUpdated('200310130000Z')
if mibBuilder.loadTexts: diffServMibCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: diffServMibCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: diffServMibCapability.setDescription('Agent capabilities for DIFFSERV-MIB')
diffServMibCapabilityMDS13R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 377, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diffServMibCapabilityMDS13R1 = diffServMibCapabilityMDS13R1.setProductRelease('Cisco MDS 1.3(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diffServMibCapabilityMDS13R1 = diffServMibCapabilityMDS13R1.setStatus('current')
if mibBuilder.loadTexts: diffServMibCapabilityMDS13R1.setDescription('DIFFSERV MIB capabilities')
mibBuilder.exportSymbols("DIFFSERV-MIB-CAPABILITY", diffServMibCapabilityMDS13R1=diffServMibCapabilityMDS13R1, diffServMibCapability=diffServMibCapability, PYSNMP_MODULE_ID=diffServMibCapability)
