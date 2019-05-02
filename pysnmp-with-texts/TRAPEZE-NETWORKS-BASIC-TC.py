#
# PySNMP MIB module TRAPEZE-NETWORKS-BASIC-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-BASIC-TC
# Produced by pysmi-0.3.4 at Wed May  1 15:27:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Gauge32, ObjectIdentity, Integer32, ModuleIdentity, TimeTicks, NotificationType, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "ObjectIdentity", "Integer32", "ModuleIdentity", "TimeTicks", "NotificationType", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzBasicTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 12))
trpzBasicTc.setRevisions(('2008-10-23 00:04',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzBasicTc.setRevisionsDescriptions(('v1.0.4: initial version, for 7.1 release',))
if mibBuilder.loadTexts: trpzBasicTc.setLastUpdated('200810230004Z')
if mibBuilder.loadTexts: trpzBasicTc.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzBasicTc.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzBasicTc.setDescription("Textual Conventions used by Trapeze Networks wireless switches. Copyright 2008 Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class TrpzIpPort(TextualConvention, Unsigned32):
    description = 'An UDP or TCP port number.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TrpzPhysPortNumber(TextualConvention, Unsigned32):
    description = 'Physical port number.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

class TrpzPhysPortNumberOrZero(TextualConvention, Unsigned32):
    description = "This textual convention is an extension of the TrpzPhysPortNumber convention. The latter defines a greater than zero value used to identify a physical port. This extension permits the additional value of zero. A zero value means 'none', 'unknown' or 'not applicable'. Each object using this textual convention should document the meaning of physical port number zero."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 1024), )
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-BASIC-TC", TrpzPhysPortNumberOrZero=TrpzPhysPortNumberOrZero, TrpzIpPort=TrpzIpPort, PYSNMP_MODULE_ID=trpzBasicTc, TrpzPhysPortNumber=TrpzPhysPortNumber, trpzBasicTc=trpzBasicTc)
