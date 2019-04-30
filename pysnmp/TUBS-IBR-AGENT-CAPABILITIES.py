#
# PySNMP MIB module TUBS-IBR-AGENT-CAPABILITIES (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-IBR-AGENT-CAPABILITIES
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Bits, Counter32, Integer32, TimeTicks, iso, MibIdentifier, Counter64, NotificationType, Unsigned32, ModuleIdentity, ObjectIdentity, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "TimeTicks", "iso", "MibIdentifier", "Counter64", "NotificationType", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibr, = mibBuilder.importSymbols("TUBS-SMI", "ibr")
ibrAgentCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 6))
ibrAgentCapabilities.setRevisions(('2000-02-09 00:00', '1998-08-05 16:23', '1997-02-14 10:23',))
if mibBuilder.loadTexts: ibrAgentCapabilities.setLastUpdated('200002090000Z')
if mibBuilder.loadTexts: ibrAgentCapabilities.setOrganization('TU Braunschweig')
linux = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 6, 1))
linuxAgent3dot3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 1575, 1, 6, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linuxAgent3dot3 = linuxAgent3dot3.setProductRelease('cmu-snmp-linux-3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linuxAgent3dot3 = linuxAgent3dot3.setStatus('current')
wwwSubagent1dot0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 1575, 1, 6, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwwSubagent1dot0 = wwwSubagent1dot0.setProductRelease('TUBS Apache WWW-MIB sub-agent version 1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwwSubagent1dot0 = wwwSubagent1dot0.setStatus('current')
mibBuilder.exportSymbols("TUBS-IBR-AGENT-CAPABILITIES", linux=linux, ibrAgentCapabilities=ibrAgentCapabilities, wwwSubagent1dot0=wwwSubagent1dot0, PYSNMP_MODULE_ID=ibrAgentCapabilities, linuxAgent3dot3=linuxAgent3dot3)
