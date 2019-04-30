#
# PySNMP MIB module CISCO-BITS-CLOCK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-BITS-CLOCK-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:34:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, NotificationType, Bits, ObjectIdentity, ModuleIdentity, MibIdentifier, Unsigned32, TimeTicks, Counter64, IpAddress, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "NotificationType", "Bits", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Unsigned32", "TimeTicks", "Counter64", "IpAddress", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoBitsClockCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 433))
ciscoBitsClockCapability.setRevisions(('2005-03-08 00:00',))
if mibBuilder.loadTexts: ciscoBitsClockCapability.setLastUpdated('200503080000Z')
if mibBuilder.loadTexts: ciscoBitsClockCapability.setOrganization('Cisco Systems, Inc.')
ciscoBitsClockV12R025000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 433, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBitsClockV12R025000SW1 = ciscoBitsClockV12R025000SW1.setProductRelease('Cisco IOS 12.2(25)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBitsClockV12R025000SW1 = ciscoBitsClockV12R025000SW1.setStatus('current')
mibBuilder.exportSymbols("CISCO-BITS-CLOCK-CAPABILITY", ciscoBitsClockCapability=ciscoBitsClockCapability, ciscoBitsClockV12R025000SW1=ciscoBitsClockV12R025000SW1, PYSNMP_MODULE_ID=ciscoBitsClockCapability)
