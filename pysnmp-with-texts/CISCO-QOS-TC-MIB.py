#
# PySNMP MIB module CISCO-QOS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-QOS-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:09:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibIdentifier, Integer32, Gauge32, Counter32, iso, TimeTicks, Counter64, NotificationType, ObjectIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "Integer32", "Gauge32", "Counter32", "iso", "TimeTicks", "Counter64", "NotificationType", "ObjectIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoQosTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 573))
ciscoQosTcMIB.setRevisions(('2007-03-05 00:00', '2006-09-18 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoQosTcMIB.setRevisionsDescriptions(('Add QosPolicerType textual convention.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoQosTcMIB.setLastUpdated('200703050000Z')
if mibBuilder.loadTexts: ciscoQosTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoQosTcMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoQosTcMIB.setDescription('This module defines the textual conventions used within Cisco Qos MIBs.')
class QosIpPrecedence(TextualConvention, Unsigned32):
    reference = 'RFC791 INTERNET PROTOCOL, Chapter 3.1'
    description = 'Indicates the IP precedence.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class QosQueueNumber(TextualConvention, Unsigned32):
    description = 'An integer indicates a queue number.'
    status = 'current'

class QosThresholdNumber(TextualConvention, Unsigned32):
    description = 'An integer indicates a threshold number.'
    status = 'current'

class QosMplsExpValue(TextualConvention, Unsigned32):
    description = 'An integer indicates a MPLS-EXP (experimental) value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class QosMutationMapName(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form, describes the name of a mutation map.'
    status = 'current'
    displayHint = '99a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 99)

class QosMutationMapNameOrEmpty(TextualConvention, OctetString):
    description = 'This textual convention is an extension of the QosMutationMapName convention. The latter defines a non-empty mutation map name. This extension permits the addtional value of empty string.'
    status = 'current'
    displayHint = '99a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 99)

class QosPolicerType(TextualConvention, Integer32):
    description = 'An integer indicating the type of a QoS policer. microflow(1): a microflow policer. aggregate(2): an aggregate policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("microflow", 1), ("aggregate", 2))

mibBuilder.exportSymbols("CISCO-QOS-TC-MIB", QosMplsExpValue=QosMplsExpValue, ciscoQosTcMIB=ciscoQosTcMIB, QosQueueNumber=QosQueueNumber, QosPolicerType=QosPolicerType, QosIpPrecedence=QosIpPrecedence, QosMutationMapNameOrEmpty=QosMutationMapNameOrEmpty, PYSNMP_MODULE_ID=ciscoQosTcMIB, QosThresholdNumber=QosThresholdNumber, QosMutationMapName=QosMutationMapName)
