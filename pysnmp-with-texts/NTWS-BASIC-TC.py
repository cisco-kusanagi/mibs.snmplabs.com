#
# PySNMP MIB module NTWS-BASIC-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-BASIC-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:25:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, ObjectIdentity, Gauge32, Unsigned32, NotificationType, Counter32, Integer32, MibIdentifier, TimeTicks, Bits, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "NotificationType", "Counter32", "Integer32", "MibIdentifier", "TimeTicks", "Bits", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsBasicTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 12))
ntwsBasicTc.setRevisions(('2008-10-23 00:04',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntwsBasicTc.setRevisionsDescriptions(('v1.0.4: initial version',))
if mibBuilder.loadTexts: ntwsBasicTc.setLastUpdated('200810230004Z')
if mibBuilder.loadTexts: ntwsBasicTc.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: ntwsBasicTc.setContactInfo('www.nortelnetworks.com')
if mibBuilder.loadTexts: ntwsBasicTc.setDescription("Textual Conventions used by Nortel Networks wireless switches. Copyright 2008 Nortel Networks. All rights reserved. This Nortel Networks SNMP Management Information Base Specification (Specification) embodies Nortel Networks' confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class NtwsIpPort(TextualConvention, Unsigned32):
    description = 'An UDP or TCP port number.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class NtwsPhysPortNumber(TextualConvention, Unsigned32):
    description = 'Physical port number.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

class NtwsPhysPortNumberOrZero(TextualConvention, Unsigned32):
    description = "This textual convention is an extension of the NtwsPhysPortNumber convention. The latter defines a greater than zero value used to identify a physical port. This extension permits the additional value of zero. A zero value means 'none', 'unknown' or 'not applicable'. Each object using this textual convention should document the meaning of physical port number zero."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 1024), )
mibBuilder.exportSymbols("NTWS-BASIC-TC", NtwsPhysPortNumberOrZero=NtwsPhysPortNumberOrZero, PYSNMP_MODULE_ID=ntwsBasicTc, NtwsPhysPortNumber=NtwsPhysPortNumber, NtwsIpPort=NtwsIpPort, ntwsBasicTc=ntwsBasicTc)
