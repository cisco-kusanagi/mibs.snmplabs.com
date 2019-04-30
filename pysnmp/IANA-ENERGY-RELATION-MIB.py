#
# PySNMP MIB module IANA-ENERGY-RELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-ENERGY-RELATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:48:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, iso, Gauge32, TimeTicks, Bits, Counter32, Counter64, mib_2, IpAddress, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "iso", "Gauge32", "TimeTicks", "Bits", "Counter32", "Counter64", "mib-2", "IpAddress", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaEnergyRelationMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 232))
ianaEnergyRelationMIB.setRevisions(('2015-02-09 00:00',))
if mibBuilder.loadTexts: ianaEnergyRelationMIB.setLastUpdated('201502090000Z')
if mibBuilder.loadTexts: ianaEnergyRelationMIB.setOrganization('IANA')
class IANAEnergyRelationship(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("poweredBy", 1), ("powering", 2), ("meteredBy", 3), ("metering", 4), ("aggregatedBy", 5), ("aggregating", 6))

mibBuilder.exportSymbols("IANA-ENERGY-RELATION-MIB", ianaEnergyRelationMIB=ianaEnergyRelationMIB, IANAEnergyRelationship=IANAEnergyRelationship, PYSNMP_MODULE_ID=ianaEnergyRelationMIB)
