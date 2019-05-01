#
# PySNMP MIB module UUID-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UUID-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:04:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
mib_2, Bits, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, TimeTicks, Counter32, Counter64, ObjectIdentity, Unsigned32, IpAddress, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Bits", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "TimeTicks", "Counter32", "Counter64", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
uuidTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 217))
uuidTCMIB.setRevisions(('2013-04-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: uuidTCMIB.setRevisionsDescriptions(('Initial version of this MIB as published in RFC 6933.',))
if mibBuilder.loadTexts: uuidTCMIB.setLastUpdated('201304050000Z')
if mibBuilder.loadTexts: uuidTCMIB.setOrganization('IETF Energy Management Working Group')
if mibBuilder.loadTexts: uuidTCMIB.setContactInfo('WG Email: eman@ietf.org Mailing list subscription info: http://www.ietf.org/mailman/listinfo/eman Dan Romascanu Avaya Park Atidim, Bldg. #3 Tel Aviv, 61581 Israel Phone: +972-3-6458414 Email: dromasca@avaya.com Juergen Quittek NEC Europe Ltd. Network Research Division Kurfuersten-Anlage 36 Heidelberg 69115 Germany Phone: +49 6221 4342-115 Email: quittek@neclab.eu Mouli Chandramouli Cisco Systems, Inc. Sarjapur Outer Ring Road Bangalore 560103 India Phone: +91 80 4429 2409 Email: moulchan@cisco.com')
if mibBuilder.loadTexts: uuidTCMIB.setDescription("This MIB module defines TEXTUAL-CONVENTIONs representing Universally Unique IDentifiers (UUIDs). Copyright (c) 2013 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info).")
class UUID(TextualConvention, OctetString):
    description = 'Universally Unique Identifier information. The syntax must conform to RFC 4122, Section 4.1.'
    status = 'current'
    displayHint = '4x-2x-2x-1x1x-6x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class UUIDorZero(TextualConvention, OctetString):
    description = 'Universally Unique Identifier information. The syntax must conform to RFC 4122, Section 4.1. The semantics of the value zero-length OCTET STRING are object-specific and must therefore be defined as part of the description of any object that uses this syntax.'
    status = 'current'
    displayHint = '4x-2x-2x-1x1x-6x'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
mibBuilder.exportSymbols("UUID-TC-MIB", UUIDorZero=UUIDorZero, PYSNMP_MODULE_ID=uuidTCMIB, uuidTCMIB=uuidTCMIB, UUID=UUID)
