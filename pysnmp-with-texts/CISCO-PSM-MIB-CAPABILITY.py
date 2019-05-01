#
# PySNMP MIB module CISCO-PSM-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PSM-MIB-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, ObjectIdentity, TimeTicks, Bits, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, ModuleIdentity, Gauge32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "ObjectIdentity", "TimeTicks", "Bits", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "ModuleIdentity", "Gauge32", "iso", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoPsmMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoPsmMibCapability.setRevisions(('2003-08-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPsmMibCapability.setRevisionsDescriptions(('The capabilities description of Cisco Port Security MIB for MDS 1.2(1).',))
if mibBuilder.loadTexts: ciscoPsmMibCapability.setLastUpdated('200308050000Z')
if mibBuilder.loadTexts: ciscoPsmMibCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPsmMibCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoPsmMibCapability.setDescription('Agent capabilities for CISCO-PSM-MIB')
ciscoPsmMibCapabilityMDS12R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsmMibCapabilityMDS12R0 = ciscoPsmMibCapabilityMDS12R0.setProductRelease('Cisco MDS 1.2(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsmMibCapabilityMDS12R0 = ciscoPsmMibCapabilityMDS12R0.setStatus('current')
if mibBuilder.loadTexts: ciscoPsmMibCapabilityMDS12R0.setDescription('Cisco Port Security MIB capabilities')
mibBuilder.exportSymbols("CISCO-PSM-MIB-CAPABILITY", ciscoPsmMibCapability=ciscoPsmMibCapability, PYSNMP_MODULE_ID=ciscoPsmMibCapability, ciscoPsmMibCapabilityMDS12R0=ciscoPsmMibCapabilityMDS12R0)
