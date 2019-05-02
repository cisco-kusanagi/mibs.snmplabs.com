#
# PySNMP MIB module CISCO-BITS-CLOCK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-BITS-CLOCK-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:51:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ObjectIdentity, MibIdentifier, IpAddress, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Counter64, Integer32, NotificationType, Bits, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Counter64", "Integer32", "NotificationType", "Bits", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoBitsClockCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 433))
ciscoBitsClockCapability.setRevisions(('2005-03-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoBitsClockCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoBitsClockCapability.setLastUpdated('200503080000Z')
if mibBuilder.loadTexts: ciscoBitsClockCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoBitsClockCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoBitsClockCapability.setDescription('Agent capabilities for the CISCO-BITS-CLOCK-MIB.')
ciscoBitsClockV12R025000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 433, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBitsClockV12R025000SW1 = ciscoBitsClockV12R025000SW1.setProductRelease('Cisco IOS 12.2(25)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBitsClockV12R025000SW1 = ciscoBitsClockV12R025000SW1.setStatus('current')
if mibBuilder.loadTexts: ciscoBitsClockV12R025000SW1.setDescription('IOS 12.2(25)SW1 Cisco CISCO-BITS-CLOCK-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-BITS-CLOCK-CAPABILITY", PYSNMP_MODULE_ID=ciscoBitsClockCapability, ciscoBitsClockV12R025000SW1=ciscoBitsClockV12R025000SW1, ciscoBitsClockCapability=ciscoBitsClockCapability)
