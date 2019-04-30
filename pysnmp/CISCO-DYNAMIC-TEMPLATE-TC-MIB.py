#
# PySNMP MIB module CISCO-DYNAMIC-TEMPLATE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DYNAMIC-TEMPLATE-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:39:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Counter64, ObjectIdentity, TimeTicks, Bits, Counter32, Integer32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Counter64", "ObjectIdentity", "TimeTicks", "Bits", "Counter32", "Integer32", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDynamicTemplateTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 783))
ciscoDynamicTemplateTcMIB.setRevisions(('2007-09-06 00:00',))
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setLastUpdated('201201270000Z')
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setOrganization('Cisco Systems, Inc.')
class DynamicTemplateName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class DynamicTemplateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("derived", 2), ("ppp", 3), ("ethernet", 4), ("ipSubscriber", 5), ("service", 6))

class DynamicTemplateTargetType(TextualConvention, Integer32):
    reference = "K. McCloghrie and F. Kastenholtz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("other", 1), ("interface", 2))

class DynamicTemplateTargetId(TextualConvention, OctetString):
    reference = "K. McCloghrie and F. Kastenholtz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

mibBuilder.exportSymbols("CISCO-DYNAMIC-TEMPLATE-TC-MIB", DynamicTemplateType=DynamicTemplateType, DynamicTemplateTargetType=DynamicTemplateTargetType, ciscoDynamicTemplateTcMIB=ciscoDynamicTemplateTcMIB, DynamicTemplateName=DynamicTemplateName, PYSNMP_MODULE_ID=ciscoDynamicTemplateTcMIB, DynamicTemplateTargetId=DynamicTemplateTargetId)
