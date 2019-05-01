#
# PySNMP MIB module IANA-ENERGY-RELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-ENERGY-RELATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:02:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Unsigned32, Gauge32, IpAddress, Counter32, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, TimeTicks, Bits, iso, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Unsigned32", "Gauge32", "IpAddress", "Counter32", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Bits", "iso", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaEnergyRelationMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 232))
ianaEnergyRelationMIB.setRevisions(('2015-02-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaEnergyRelationMIB.setRevisionsDescriptions(('Initial version of this MIB as published in RFC 7461.',))
if mibBuilder.loadTexts: ianaEnergyRelationMIB.setLastUpdated('201502090000Z')
if mibBuilder.loadTexts: ianaEnergyRelationMIB.setOrganization('IANA')
if mibBuilder.loadTexts: ianaEnergyRelationMIB.setContactInfo(' Internet Assigned Numbers Authority Postal: ICANN 12025 Waterfront Dr., Suite 300 Los Angeles, CA 90094 United States Tel: +1-310-301-5800 EMail: iana&iana.org')
if mibBuilder.loadTexts: ianaEnergyRelationMIB.setDescription("Copyright (c) 2015 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). This MIB module defines a TEXTUAL-CONVENTION that describes the relationships between Energy Objects. The initial version of this MIB module was published in RFC 7461; for full legal notices see the RFC itself.")
class IANAEnergyRelationship(TextualConvention, Integer32):
    description = "An enumerated value specifying the type of relationship between an Energy Object A, on which the relationship is specified, with the Energy Object B, identified by the UUID. The enumeration 'poweredBy' is applicable if Energy Object A is poweredBy Energy Object B. The enumeration 'powering' is applicable if Energy Object A is powering Energy Object B. The enumeration 'meteredBy' is applicable if Energy Object A is meteredBy Energy Object B. The enumeration 'metering' is applicable if Energy Object A is metering Energy Object B. The enumeration 'aggregatedBy' is applicable if Energy Object A is aggregatedBy Energy Object B. The enumeration 'aggregating' is applicable if Energy Object A is aggregating Energy Object B."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("poweredBy", 1), ("powering", 2), ("meteredBy", 3), ("metering", 4), ("aggregatedBy", 5), ("aggregating", 6))

mibBuilder.exportSymbols("IANA-ENERGY-RELATION-MIB", ianaEnergyRelationMIB=ianaEnergyRelationMIB, IANAEnergyRelationship=IANAEnergyRelationship, PYSNMP_MODULE_ID=ianaEnergyRelationMIB)
