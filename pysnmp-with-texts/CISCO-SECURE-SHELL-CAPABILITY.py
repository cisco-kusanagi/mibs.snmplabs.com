#
# PySNMP MIB module CISCO-SECURE-SHELL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SECURE-SHELL-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:11:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter32, TimeTicks, Counter64, NotificationType, ModuleIdentity, Unsigned32, MibIdentifier, iso, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Counter64", "NotificationType", "ModuleIdentity", "Unsigned32", "MibIdentifier", "iso", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Integer32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ciscoSecureShellCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoSecureShellCapability.setRevisions(('2004-04-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSecureShellCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSecureShellCapability.setLastUpdated('200404190000Z')
if mibBuilder.loadTexts: ciscoSecureShellCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSecureShellCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSecureShellCapability.setDescription('The capabilities description of CISCO-SECURE-SHELL-MIB.')
cSecureShellCapCatOSV08R0401k9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSecureShellCapCatOSV08R0401k9 = cSecureShellCapCatOSV08R0401k9.setProductRelease('Cisco CatOS 8.4(1) cryptographic\n                         software with Secure Shell support.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSecureShellCapCatOSV08R0401k9 = cSecureShellCapCatOSV08R0401k9.setStatus('current')
if mibBuilder.loadTexts: cSecureShellCapCatOSV08R0401k9.setDescription('CISCO-SECURE-SHELL-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SECURE-SHELL-CAPABILITY", cSecureShellCapCatOSV08R0401k9=cSecureShellCapCatOSV08R0401k9, PYSNMP_MODULE_ID=ciscoSecureShellCapability, ciscoSecureShellCapability=ciscoSecureShellCapability)
