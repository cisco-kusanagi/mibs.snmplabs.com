#
# PySNMP MIB module ALCATEL-IND1-SNMP-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-SNMP-AGENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:19:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1SnmpAgt, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1SnmpAgt")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, IpAddress, NotificationType, Counter32, TimeTicks, Counter64, ModuleIdentity, MibIdentifier, iso, ObjectIdentity, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "IpAddress", "NotificationType", "Counter32", "TimeTicks", "Counter64", "ModuleIdentity", "MibIdentifier", "iso", "ObjectIdentity", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1SNMPAgentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1))
alcatelIND1SNMPAgentMIB.setRevisions(('2007-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setRevisionsDescriptions(('Addressing discrepancies with Alcatel Standard.',))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setDescription('This module describes an authoritative enterprise-specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): For the Birds Of Prey Product Line SNMP Agent Subsystem. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2007 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1SNMPAgentMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBObjects.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBObjects.setDescription('Branch For SNMP Agent Subsystem Managed Objects.')
alcatelIND1SNMPAgentMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBConformance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBConformance.setDescription('Branch For SNMP Agent Subsystem Conformance Information.')
alcatelIND1SNMPAgentMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBGroups.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBGroups.setDescription('Branch For SNMP Agent Subsystem Units Of Conformance.')
alcatelIND1SNMPAgentMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBCompliances.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBCompliances.setDescription('Branch For SNMP Agent Subsystem Compliance Statements.')
snmpAgtConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 1))
class SnmpAgtSecurityLevel(TextualConvention, Integer32):
    description = 'The switch security level'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noSec", 1), ("authSet", 2), ("authAll", 3), ("privSet", 4), ("privAll", 5), ("trapOnly", 6))

snmpAgtSecurityLevel = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 1, 1), SnmpAgtSecurityLevel().clone('noSec')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtSecurityLevel.setStatus('current')
if mibBuilder.loadTexts: snmpAgtSecurityLevel.setDescription('Level of security required for SNMP get or SET. noSec: no security; all the PDU with a known user id are accepted authSet: authentication required for set; all GET are accepted, but not authenticated SET are rejected. authAll: authentication required for SET and GET; not authenticated SET and GET are rejected. privSet: authentication required for GET and encryption required for SET. privAll: encryption required for SET and GET. trapOnly: no SNMP GET or SET are accepted.')
snmpAgtCommunityMode = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtCommunityMode.setStatus('current')
if mibBuilder.loadTexts: snmpAgtCommunityMode.setDescription('If the community mode is enabled, the SNMPv1/v2 packets must use the community names.')
snmpAgtCtlFiles = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 3))
if mibBuilder.loadTexts: snmpAgtCtlFiles.setStatus('current')
if mibBuilder.loadTexts: snmpAgtCtlFiles.setDescription('MIB entity on which to attach the MODULE-IDENTITY for the Epilogue(R) control files.')
snmpAgtSourceIpConfig = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("default", 1), ("noLoopback0", 2), ("ipInterface", 3))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtSourceIpConfig.setStatus('current')
if mibBuilder.loadTexts: snmpAgtSourceIpConfig.setDescription('The SNMP Agent Configuration 1 -- Default(Loopback0 or closest IP) 2 -- No Loopback0 3 -- Interface IP Specified by User')
snmpAgtSourceIp = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtSourceIp.setStatus('current')
if mibBuilder.loadTexts: snmpAgtSourceIp.setDescription('The Source IP of SNMP Packets')
alcatelIND1SNMPAgentMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1SNMPAgentMIBCompliance = alcatelIND1SNMPAgentMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBCompliance.setDescription('Compliance statement for SNMP Agent Subsystem.')
snmpAgtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSecurityLevel"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtCommunityMode"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSourceIp"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSourceIpConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpAgtConfigGroup = snmpAgtConfigGroup.setStatus('current')
if mibBuilder.loadTexts: snmpAgtConfigGroup.setDescription('Collection of objects for SNMP Agent configuration.')
mibBuilder.exportSymbols("ALCATEL-IND1-SNMP-AGENT-MIB", snmpAgtSourceIpConfig=snmpAgtSourceIpConfig, alcatelIND1SNMPAgentMIB=alcatelIND1SNMPAgentMIB, alcatelIND1SNMPAgentMIBConformance=alcatelIND1SNMPAgentMIBConformance, alcatelIND1SNMPAgentMIBCompliance=alcatelIND1SNMPAgentMIBCompliance, alcatelIND1SNMPAgentMIBObjects=alcatelIND1SNMPAgentMIBObjects, SnmpAgtSecurityLevel=SnmpAgtSecurityLevel, snmpAgtSecurityLevel=snmpAgtSecurityLevel, alcatelIND1SNMPAgentMIBCompliances=alcatelIND1SNMPAgentMIBCompliances, snmpAgtCtlFiles=snmpAgtCtlFiles, snmpAgtCommunityMode=snmpAgtCommunityMode, snmpAgtSourceIp=snmpAgtSourceIp, snmpAgtConfigGroup=snmpAgtConfigGroup, alcatelIND1SNMPAgentMIBGroups=alcatelIND1SNMPAgentMIBGroups, snmpAgtConfig=snmpAgtConfig, PYSNMP_MODULE_ID=alcatelIND1SNMPAgentMIB)
