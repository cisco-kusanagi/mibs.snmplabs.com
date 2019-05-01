#
# PySNMP MIB module TPT-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-LICENSE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, IpAddress, MibIdentifier, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Counter32, Counter64, NotificationType, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "IpAddress", "MibIdentifier", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Counter32", "Counter64", "NotificationType", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_license_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15)).setLabel("tpt-license-objs")
tpt_license_objs.setRevisions(('2016-05-25 18:54',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpt_license_objs.setRevisionsDescriptions(('Updated copyright information. Minor MIB syntax fixes.',))
if mibBuilder.loadTexts: tpt_license_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_license_objs.setOrganization('Trend Micro, Inc.')
if mibBuilder.loadTexts: tpt_license_objs.setContactInfo('www.trendmicro.com')
if mibBuilder.loadTexts: tpt_license_objs.setDescription("License Package support. Copyright (C) 2016 Trend Micro Incorporated. All Rights Reserved. Trend Micro makes no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Trend Micro shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material. This document contains proprietary information, which is protected by copyright. No part of this document may be photocopied, reproduced, or translated into another language without the prior written consent of Trend Micro. The information is provided 'as is' without warranty of any kind and is subject to change without notice. The only warranties for Trend Micro products and services are set forth in the express warranty statements accompanying such products and services. Nothing herein should be construed as constituting an additional warranty. Trend Micro shall not be liable for technical or editorial errors or omissions contained herein. TippingPoint(R), the TippingPoint logo, and Digital Vaccine(R) are registered trademarks of Trend Micro. All other company and product names may be trademarks of their respective holders. All rights reserved. This document contains confidential information, trade secrets or both, which are the property of Trend Micro. No part of this documentation may be reproduced in any form or by any means or used to make any derivative work (such as translation, transformation, or adaptation) without written permission from Trend Micro or one of its subsidiaries. All other company and product names may be trademarks of their respective holders. ")
class LicenseStatus(TextualConvention, Integer32):
    description = 'An indicator of the status for a licensed feature.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("info", 0), ("ok", 1), ("warning", 2), ("error", 3))

class LicenseAction(TextualConvention, Integer32):
    description = 'The action to take for a licensed feature.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("allow", 0), ("deny", 1))

licenseTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1), )
if mibBuilder.loadTexts: licenseTable.setStatus('current')
if mibBuilder.loadTexts: licenseTable.setDescription('Table of licensed features.')
licenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1), ).setIndexNames((0, "TPT-LICENSE-MIB", "licenseEntryIndex"))
if mibBuilder.loadTexts: licenseEntry.setStatus('current')
if mibBuilder.loadTexts: licenseEntry.setDescription('An entry in the licensed feature table. Rows cannot be created or deleted.')
licenseEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: licenseEntryIndex.setStatus('current')
if mibBuilder.loadTexts: licenseEntryIndex.setDescription('Index into the licensed feature table, starting with 1.')
licenseEntryFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryFeature.setStatus('current')
if mibBuilder.loadTexts: licenseEntryFeature.setDescription('The name of the licensed feature.')
licenseEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 3), LicenseStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryStatus.setStatus('current')
if mibBuilder.loadTexts: licenseEntryStatus.setDescription('Status of this licensed feature.')
licenseEntryAction = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 4), LicenseAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryAction.setStatus('current')
if mibBuilder.loadTexts: licenseEntryAction.setDescription('Action to take for this licensed feature.')
licenseEntryExpiry = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryExpiry.setStatus('current')
if mibBuilder.loadTexts: licenseEntryExpiry.setDescription('The date on which this licensed feature will expire.')
licenseEntryDetails = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryDetails.setStatus('current')
if mibBuilder.loadTexts: licenseEntryDetails.setDescription('Any additional information about this licensed feature.')
mibBuilder.exportSymbols("TPT-LICENSE-MIB", licenseEntryAction=licenseEntryAction, licenseTable=licenseTable, licenseEntryIndex=licenseEntryIndex, licenseEntryExpiry=licenseEntryExpiry, licenseEntryStatus=licenseEntryStatus, LicenseAction=LicenseAction, licenseEntry=licenseEntry, licenseEntryDetails=licenseEntryDetails, LicenseStatus=LicenseStatus, PYSNMP_MODULE_ID=tpt_license_objs, licenseEntryFeature=licenseEntryFeature, tpt_license_objs=tpt_license_objs)
