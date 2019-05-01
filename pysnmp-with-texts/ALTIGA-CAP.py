#
# PySNMP MIB module ALTIGA-CAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTIGA-CAP
# Produced by pysmi-0.3.4 at Wed May  1 11:21:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alCapModule, altigaCaps = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alCapModule", "altigaCaps")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, Bits, iso, Integer32, NotificationType, Gauge32, ObjectIdentity, Counter32, TimeTicks, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "Bits", "iso", "Integer32", "NotificationType", "Gauge32", "ObjectIdentity", "Counter32", "TimeTicks", "ModuleIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaCapModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 2, 1))
altigaCapModule.setRevisions(('2002-09-09 12:00', '2002-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaCapModule.setRevisionsDescriptions(('Updated MIB to comply to Cisco MIB Police standards. Added missing supports for new Altiga MIBs. ', 'Updated with new header',))
if mibBuilder.loadTexts: altigaCapModule.setLastUpdated('200209091200Z')
if mibBuilder.loadTexts: altigaCapModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaCapModule.setContactInfo('Cisco Systems 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaCapModule.setDescription('The Altiga Networks capabilities MIB models counters and objects that are of management interest for networks capabilities. Acronyms The following acronyms are used in this document: DHCP: Dynamic Host Configuration Protocol DNS: Domain Name Service FTP: File Transfer Protocol HTTP: HyperText Transfer Protocol ICMP: Internet Control Message Protocol IP: Internet Protocol L2TP: Layer-2 Tunneling Protocol MIB: Management Information Base PPP: Point-to-Point Protocol PPTP: Point-to-Point Tunneling Protocol SEP: Scalable Encryption Processor SNMP: Simple Network Management Protocol SSL: Secure Sockets Layer TCP: Transmission Control Protocol UDP: User Datagram Protocol ')
altigaBasicAgent = AgentCapabilities((1, 3, 6, 1, 4, 1, 3076, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaBasicAgent = altigaBasicAgent.setProductRelease('Altiga Agent v1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaBasicAgent = altigaBasicAgent.setStatus('obsolete')
if mibBuilder.loadTexts: altigaBasicAgent.setDescription('Altiga SNMP Agent')
altigaBasicAgentRev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 3076, 1, 1, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaBasicAgentRev1 = altigaBasicAgentRev1.setProductRelease('Altiga Agent v1.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaBasicAgentRev1 = altigaBasicAgentRev1.setStatus('current')
if mibBuilder.loadTexts: altigaBasicAgentRev1.setDescription('Altiga SNMP Agent')
mibBuilder.exportSymbols("ALTIGA-CAP", altigaBasicAgentRev1=altigaBasicAgentRev1, altigaCapModule=altigaCapModule, PYSNMP_MODULE_ID=altigaCapModule, altigaBasicAgent=altigaBasicAgent)
