#
# PySNMP MIB module IANA-GBOND-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-GBOND-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:18:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, TimeTicks, ObjectIdentity, Unsigned32, Gauge32, Counter32, Counter64, MibIdentifier, Bits, Integer32, mib_2, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "TimeTicks", "ObjectIdentity", "Unsigned32", "Gauge32", "Counter32", "Counter64", "MibIdentifier", "Bits", "Integer32", "mib-2", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaGBondTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 215))
ianaGBondTcMIB.setRevisions(('2013-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaGBondTcMIB.setRevisionsDescriptions(('Initial version, published as RFC 6765.',))
if mibBuilder.loadTexts: ianaGBondTcMIB.setLastUpdated('201302200000Z')
if mibBuilder.loadTexts: ianaGBondTcMIB.setOrganization('IANA')
if mibBuilder.loadTexts: ianaGBondTcMIB.setContactInfo(' Internet Assigned Numbers Authority Postal: ICANN 12025 Waterfront Drive, Suite 300 Los Angeles, CA 90094-2536 Tel: +1-310-301-5800 EMail: iana@iana.org')
if mibBuilder.loadTexts: ianaGBondTcMIB.setDescription("This MIB module defines IANAgBondScheme and IANAgBondSchemeList TEXTUAL-CONVENTIONs, specifying enumerated values of the gBondPortConfAdminScheme, gBondPortConfPeerAdminScheme, gBondPortStatOperScheme, gBondPortStatPeerOperScheme, gBondPortCapSchemesSupported, and gBondPortCapPeerSchemesSupported objects, respectively, as defined in the GBOND-MIB. It is intended that each new bonding scheme defined by the ITU-T Q4/SG15 working group and approved for publication in a revision of the ITU-T G.998 specification will be added to this MIB module, provided that it is suitable for being managed by the base objects in the GBOND-MIB. An Expert Review, as defined in RFC 5226, is REQUIRED for such additions. The following references are used throughout this MIB module: [G.998.1] refers to: ITU-T Recommendation G.998.1: 'ATM-based multi-pair bonding', January 2005. [G.998.2] refers to: ITU-T Recommendation G.998.2: 'Ethernet-based multi-pair bonding', January 2005. [G.998.3] refers to: ITU-T Recommendation G.998.3: 'Multi-pair bonding using time-division inverse multiplexing', January 2005. Naming Conventions: BCE - Bonding Channel Entity GBS - Generic Bonding Sub-layer These references should be updated as appropriate when a new bonding scheme is added to this MIB module. Copyright (c) 2013 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info).")
class IANAgBondSchemeList(TextualConvention, Bits):
    description = 'This textual convention defines a bitmap of possible ITU-T G.998 (G.Bond) bonding schemes. Currently, the following values are defined for the corresponding bonding schemes: g9981(1) - G.998.1 (G.Bond/ATM; see the G9981-MIB) g9982(2) - G.998.2 (G.Bond/Ethernet; see the G9982-MIB) g9983(3) - G.998.3 (G.Bond/TDIM; see the G9983-MIB) An additional value of none(0) can be returned as a result of a GET operation when a value of the object cannot be determined (for example, a peer GBS cannot be reached), the port does not support any kind of bonding, or when a single-BCE G.998.2 GBS supports bonding (frame fragmentation/reassembly) bypass.'
    status = 'current'
    namedValues = NamedValues(("none", 0), ("g9981", 1), ("g9982", 2), ("g9983", 3))

class IANAgBondScheme(TextualConvention, Integer32):
    description = 'This textual convention defines ITU-T G.998 bonding scheme values. Possible values are: none(0) - no bonding (e.g., on a single-BCE G.998.2 GBS) or unknown g9981(1) - G.998.1 (G.Bond/ATM) g9982(2) - G.998.2 (G.Bond/Ethernet) g9983(3) - G.998.3 (G.Bond/TDIM)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("g9981", 1), ("g9982", 2), ("g9983", 3))

mibBuilder.exportSymbols("IANA-GBOND-TC-MIB", ianaGBondTcMIB=ianaGBondTcMIB, PYSNMP_MODULE_ID=ianaGBondTcMIB, IANAgBondScheme=IANAgBondScheme, IANAgBondSchemeList=IANAgBondSchemeList)
