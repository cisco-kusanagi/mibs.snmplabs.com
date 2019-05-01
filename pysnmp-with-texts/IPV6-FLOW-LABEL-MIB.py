#
# PySNMP MIB module IPV6-FLOW-LABEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPV6-FLOW-LABEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:07:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Bits, Counter64, Counter32, ObjectIdentity, TimeTicks, IpAddress, NotificationType, Integer32, Unsigned32, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Bits", "Counter64", "Counter32", "ObjectIdentity", "TimeTicks", "IpAddress", "NotificationType", "Integer32", "Unsigned32", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ipv6FlowLabelMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 103))
ipv6FlowLabelMIB.setRevisions(('2003-08-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipv6FlowLabelMIB.setRevisionsDescriptions(('Initial version, published as RFC 3595.',))
if mibBuilder.loadTexts: ipv6FlowLabelMIB.setLastUpdated('200308280000Z')
if mibBuilder.loadTexts: ipv6FlowLabelMIB.setOrganization('IETF Operations and Management Area')
if mibBuilder.loadTexts: ipv6FlowLabelMIB.setContactInfo('Bert Wijnen (Editor) Lucent Technologies Schagen 33 3461 GL Linschoten Netherlands Phone: +31 348-407-775 EMail: bwijnen@lucent.com Send comments to <mibs@ops.ietf.org>. ')
if mibBuilder.loadTexts: ipv6FlowLabelMIB.setDescription('This MIB module provides commonly used textual conventions for IPv6 Flow Labels. Copyright (C) The Internet Society (2003). This version of this MIB module is part of RFC 3595, see the RFC itself for full legal notices. ')
class IPv6FlowLabel(TextualConvention, Integer32):
    reference = 'Internet Protocol, Version 6 (IPv6) specification, section 6. RFC 2460. '
    description = 'The flow identifier or Flow Label in an IPv6 packet header that may be used to discriminate traffic flows. '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1048575)

class IPv6FlowLabelOrAny(TextualConvention, Integer32):
    description = 'The flow identifier or Flow Label in an IPv6 packet header that may be used to discriminate traffic flows. The value of -1 is used to indicate a wildcard, i.e. any value. '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1048575), )
mibBuilder.exportSymbols("IPV6-FLOW-LABEL-MIB", IPv6FlowLabel=IPv6FlowLabel, ipv6FlowLabelMIB=ipv6FlowLabelMIB, PYSNMP_MODULE_ID=ipv6FlowLabelMIB, IPv6FlowLabelOrAny=IPv6FlowLabelOrAny)
