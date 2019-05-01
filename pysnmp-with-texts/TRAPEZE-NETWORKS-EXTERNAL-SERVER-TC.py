#
# PySNMP MIB module TRAPEZE-NETWORKS-EXTERNAL-SERVER-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-EXTERNAL-SERVER-TC
# Produced by pysmi-0.3.4 at Wed May  1 15:27:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, Counter32, Gauge32, ObjectIdentity, Integer32, ModuleIdentity, TimeTicks, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "Counter32", "Gauge32", "ObjectIdentity", "Integer32", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzExternalServerTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 23))
trpzExternalServerTc.setRevisions(('2012-02-16 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzExternalServerTc.setRevisionsDescriptions(('v1.0.0: initial version, for 7.7 release',))
if mibBuilder.loadTexts: trpzExternalServerTc.setLastUpdated('201202160001Z')
if mibBuilder.loadTexts: trpzExternalServerTc.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzExternalServerTc.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzExternalServerTc.setDescription("Textual Conventions used by Trapeze Networks wireless switches. Copyright 2012 Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class TrpzSyslogSeverity(TextualConvention, Integer32):
    reference = 'RFC 5424, section 6.2.1.'
    description = 'The severity levels of syslog messages. The enumeration values are equal to the actual values that syslog uses + 1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("informational", 7), ("debug", 8))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-EXTERNAL-SERVER-TC", TrpzSyslogSeverity=TrpzSyslogSeverity, trpzExternalServerTc=trpzExternalServerTc, PYSNMP_MODULE_ID=trpzExternalServerTc)
