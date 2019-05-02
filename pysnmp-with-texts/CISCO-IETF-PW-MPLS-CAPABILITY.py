#
# PySNMP MIB module CISCO-IETF-PW-MPLS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PW-MPLS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Gauge32, ModuleIdentity, Integer32, Bits, NotificationType, IpAddress, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "NotificationType", "IpAddress", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "ObjectIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cpwVcMplsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 429))
cpwVcMplsCapability.setRevisions(('2004-10-06 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cpwVcMplsCapability.setRevisionsDescriptions(('Made Cisco proprietary based on the PW-MPLS-MIB.my file extracted from draft-ietf-pwe3-pw-mpls-mib-00.txt',))
if mibBuilder.loadTexts: cpwVcMplsCapability.setLastUpdated('200410061200Z')
if mibBuilder.loadTexts: cpwVcMplsCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cpwVcMplsCapability.setContactInfo('Thomas D. Nadeau Postal: Cisco Systems, Inc. 250 Apollo Drive Chelmsford, MA 01824 Tel: +1-978-497-3051 Email: tnadeau@cisco.com MPLS MIB Development Team Postal: Cisco Systems, Inc. 250 Apollo Drive Chelmsford, MA 01924 Tel: +1-978-497-3989 Email: ch-mpls-mib-dev@cisco.com ')
if mibBuilder.loadTexts: cpwVcMplsCapability.setDescription('Agent capabilities for CISCO-IETF-PW-MPLS-MIB')
cpwVcMplsCapability1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 429, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcMplsCapability1 = cpwVcMplsCapability1.setProductRelease('Cisco IOS 12.0(29)S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcMplsCapability1 = cpwVcMplsCapability1.setStatus('current')
if mibBuilder.loadTexts: cpwVcMplsCapability1.setDescription('pseudowire over MPLS MIB capabilities')
mibBuilder.exportSymbols("CISCO-IETF-PW-MPLS-CAPABILITY", cpwVcMplsCapability=cpwVcMplsCapability, PYSNMP_MODULE_ID=cpwVcMplsCapability, cpwVcMplsCapability1=cpwVcMplsCapability1)
