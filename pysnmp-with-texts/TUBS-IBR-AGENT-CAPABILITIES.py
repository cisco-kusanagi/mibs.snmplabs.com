#
# PySNMP MIB module TUBS-IBR-AGENT-CAPABILITIES (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-IBR-AGENT-CAPABILITIES
# Produced by pysmi-0.3.4 at Wed May  1 15:27:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Gauge32, ObjectIdentity, Counter64, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, MibIdentifier, Bits, Integer32, ModuleIdentity, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Counter64", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "MibIdentifier", "Bits", "Integer32", "ModuleIdentity", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibr, = mibBuilder.importSymbols("TUBS-SMI", "ibr")
ibrAgentCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 6))
ibrAgentCapabilities.setRevisions(('2000-02-09 00:00', '1998-08-05 16:23', '1997-02-14 10:23',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ibrAgentCapabilities.setRevisionsDescriptions(('Updated IMPORTS and minor stylistic fixes.', 'Added agent capabilities for the WWW-MIB subagent version 1.0.', 'The initial revision of this module.',))
if mibBuilder.loadTexts: ibrAgentCapabilities.setLastUpdated('200002090000Z')
if mibBuilder.loadTexts: ibrAgentCapabilities.setOrganization('TU Braunschweig')
if mibBuilder.loadTexts: ibrAgentCapabilities.setContactInfo('Juergen Schoenwaelder TU Braunschweig Bueltenweg 74/75 38106 Braunschweig Germany Tel: +49 531 391 3283 Fax: +49 531 391 5936 E-mail: schoenw@ibr.cs.tu-bs.de')
if mibBuilder.loadTexts: ibrAgentCapabilities.setDescription('Agent capability statements.')
linux = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 6, 1))
linuxAgent3dot3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 1575, 1, 6, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linuxAgent3dot3 = linuxAgent3dot3.setProductRelease('cmu-snmp-linux-3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linuxAgent3dot3 = linuxAgent3dot3.setStatus('current')
if mibBuilder.loadTexts: linuxAgent3dot3.setDescription('CMU SNMP v1.1b + SNMPv2 USEC + LINUX')
wwwSubagent1dot0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 1575, 1, 6, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwwSubagent1dot0 = wwwSubagent1dot0.setProductRelease('TUBS Apache WWW-MIB sub-agent version 1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwwSubagent1dot0 = wwwSubagent1dot0.setStatus('current')
if mibBuilder.loadTexts: wwwSubagent1dot0.setDescription('TUBS WWW-MIB sub-agent version 1.0 for Solaris.')
mibBuilder.exportSymbols("TUBS-IBR-AGENT-CAPABILITIES", linuxAgent3dot3=linuxAgent3dot3, ibrAgentCapabilities=ibrAgentCapabilities, PYSNMP_MODULE_ID=ibrAgentCapabilities, wwwSubagent1dot0=wwwSubagent1dot0, linux=linux)
