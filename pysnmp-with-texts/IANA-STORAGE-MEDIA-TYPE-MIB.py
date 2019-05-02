#
# PySNMP MIB module IANA-STORAGE-MEDIA-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-STORAGE-MEDIA-TYPE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, Unsigned32, IpAddress, Counter64, ObjectIdentity, Bits, MibIdentifier, iso, ModuleIdentity, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Unsigned32", "IpAddress", "Counter64", "ObjectIdentity", "Bits", "MibIdentifier", "iso", "ModuleIdentity", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaStorageMediaTypeMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 237))
ianaStorageMediaTypeMIB.setRevisions(('2015-10-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaStorageMediaTypeMIB.setRevisionsDescriptions(('The initial version of this MIB, published as RFC 7666.',))
if mibBuilder.loadTexts: ianaStorageMediaTypeMIB.setLastUpdated('201510120000Z')
if mibBuilder.loadTexts: ianaStorageMediaTypeMIB.setOrganization('IANA')
if mibBuilder.loadTexts: ianaStorageMediaTypeMIB.setContactInfo('Internet Assigned Numbers Authority Postal: ICANN 12025 Waterfront Drive, Suite 300 Los Angeles, CA 90094-2536 United States Tel: +1 310-301-5800 Email: iana&iana.org')
if mibBuilder.loadTexts: ianaStorageMediaTypeMIB.setDescription("This MIB module defines Textual Conventions representing the media type of a storage device. Copyright (c) 2015 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info).")
class IANAStorageMediaType(TextualConvention, Integer32):
    description = 'The media type of a storage device: unknown(1) The media type is unknown, e.g., because the implementation failed to obtain the media type from the hypervisor. other(2) The media type is other than those defined in this conversion. hardDisk(3) The media type is hard disk. opticalDisk(4) The media type is optical disk. floppyDisk(5) The media type is floppy disk.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("hardDisk", 3), ("opticalDisk", 4), ("floppyDisk", 5))

mibBuilder.exportSymbols("IANA-STORAGE-MEDIA-TYPE-MIB", ianaStorageMediaTypeMIB=ianaStorageMediaTypeMIB, PYSNMP_MODULE_ID=ianaStorageMediaTypeMIB, IANAStorageMediaType=IANAStorageMediaType)
