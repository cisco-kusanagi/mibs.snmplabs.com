#
# PySNMP MIB module CISCO-IETF-PW-MPLS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PW-MPLS-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, Bits, MibIdentifier, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Gauge32, Counter32, ObjectIdentity, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Bits", "MibIdentifier", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Gauge32", "Counter32", "ObjectIdentity", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cpwVcMplsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 429))
cpwVcMplsCapability.setRevisions(('2004-10-06 12:00',))
if mibBuilder.loadTexts: cpwVcMplsCapability.setLastUpdated('200410061200Z')
if mibBuilder.loadTexts: cpwVcMplsCapability.setOrganization('Cisco Systems, Inc.')
cpwVcMplsCapability1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 429, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcMplsCapability1 = cpwVcMplsCapability1.setProductRelease('Cisco IOS 12.0(29)S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcMplsCapability1 = cpwVcMplsCapability1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-PW-MPLS-CAPABILITY", cpwVcMplsCapability1=cpwVcMplsCapability1, PYSNMP_MODULE_ID=cpwVcMplsCapability, cpwVcMplsCapability=cpwVcMplsCapability)
